from controllers.request_controller import make_request , remove_request , accept_request , reject_request
from flask import Blueprint

request_bp = Blueprint('request_bp' , __name__)

@request_bp.post('/make-request')
def make_request_wrapper():
    return make_request()
    
@request_bp.delete('/remove-request')
def remove_request_wrapper():
    return remove_request()

@request_bp.post('/accept-request')
def accept_request_wrapper():
    return accept_request()

@request_bp.post('/reject-request')
def reject_request_wrapper():
    return reject_request()