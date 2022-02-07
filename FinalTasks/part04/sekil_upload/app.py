import os
from flask import Flask, render_template, request, redirect, abort, flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/sekil_upload/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "Flask_image yuklemek"
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


def allowed_file(file1):
    return '.' in file1 and \
           file1.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    

@app.route('/sekilyukleme', methods=['POST'])
def sekilyukleme():

   if request.method == 'POST':

        # formdan file gelib gelmediğini yoxlama edelim
      if 'file1' not in request.files:
         flash('file seçilmedi')
         return redirect('sekilyukleme')         

        # istifadeci file seçmemiş ve tarayıcı boş ad göndermiş mi
      file1 = request.files['file1']                    
      if file1.filename == '':
         flash('file seçilmedi')
         return redirect('sekilyukleme')

        # gelen file güvenlik sorgularindan geçir
      if file1 and allowed_file(file1.filename):
         fileadi = secure_filename(file1.filename)
         file1.save(os.path.join(app.config['UPLOAD_FOLDER'], fileadi))
         return redirect('sekilyukleme/' + fileadi)
      else:
         flash('İcaze verilmeyen file uzantısı')
         return redirect('sekilyukleme')

   else:
      abort(401)
    
@app.route('/sekilyukleme')
def sekilyukleme():
   return render_template("sekilyukleme.html")

@app.route('/sekilyukleme/<string:file1>')
def sekilyuklemenetice(file1):
   return render_template("sekilyukleme.html", file1=file1)
