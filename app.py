import cv2
import numpy as np
import os
from PIL import Image
import io
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.data.datasets import register_coco_instances
from detectron2.data import DatasetCatalog, MetadataCatalog
from flask import Flask, render_template, flash, request, redirect, send_from_directory # type: ignore
from werkzeug.utils import secure_filename # type: ignore

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = { 'png', 'jpeg', 'jpg' }

class Metadata:
    def get(self, _):
        return  ['None','Aluminium foil','Battery','Aluminium blister pack','Carded blister pack','Clear plastic bottle','Glass bottle','Other plastic bottle','Plastic bottle cap', \
                    'Metal bottle cap','Broken glass','Aerosol','Drink can','Food can','Corrugated carton','Drink carton','Egg carton','Meal carton','Pizza box','Toilet tube', \
                    'Other carton','Cigarette', 'Paper cup','Disposable plastic cup','Foam cup','Glass cup','Other plastic cup','Food waste','Glass jar','Plastic lid','Metal lid', \
                    'Normal paper','Tissues','Wrapping paper','Magazine paper','Paper bag','Plastified paper bag','Garbage bag','Single-use carrier bag','Polypropylene bag',\
                    'Plastic Film','Six pack rings','Crisp packet','Other plastic wrapper','Spread tub','Tupperware','Disposable food container','Foam food container', \
                    'Other plastic container','Plastic gloves','Plastic utensils','Pop tab','Rope','Scrap metal','Shoe','Squeezable tube','Plastic straw','Paper straw', \
                    'Styrofoam piece','Other plastic','Unlabeled litter']

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def predict(file):
    cfg = get_cfg()
    cfg.merge_from_file("static/config.yaml")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
    cfg.DATASETS.TEST = ("taco_val",)
    cfg.MODEL.DEVICE = "cpu"
    cfg.MODEL.WEIGHTS = os.path.join("static","model_final.pth")
    predictor = DefaultPredictor(cfg)

    img = cv2.imread(os.path.join(UPLOAD_FOLDER,file.filename))

    outputs = predictor(img)
    
    v = Visualizer(img[:, :, ::-1], Metadata, scale=0.5)

    result_image = v.draw_instance_predictions(outputs["instances"].to("cpu")).get_image()

    # Convert the VisImage to a NumPy array
    result_array = np.asarray(result_image)

    # Resize the image to the target size
    pil_image = Image.fromarray(result_array) 
    img_buffer = io.BytesIO()
    new_filename = "prediction_" + file.filename
    setattr(pil_image, 'filename', new_filename)

    # Save the resized image to the buffer in the specified format
    pil_image.save(img_buffer, 'PNG')

    return pil_image

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Us page
@app.route('/about')
def about():
    return render_template('AboutUs.html')

@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        file = predict(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template("index.html", uploaded_file=filename)
    else:
        flash('Invalid File Type: Allowed image types are -> png, jpg, jpeg')
        return redirect(request.url)

@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    register_coco_instances("taco_val", {}, "static/annotations_9_val.json", UPLOAD_FOLDER)
    val_dataset_dicts = DatasetCatalog.get("taco_val")
    app.secret_key = "ladfhjkh"
    app.run()