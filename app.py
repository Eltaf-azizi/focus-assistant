import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.model import get_response



# Load environment variables
load_dotenv()


os.system("python backend/ingest_data.py")


app = Flask(__name__)
CORS(app)