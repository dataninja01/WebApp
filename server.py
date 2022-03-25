
###To host website or FLask Application we can use Python Anywhere 

# https://help.pythonanywhere.com/pages/Flask/

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)
@app.route('/')
def my_home():
    # return 'Hello, Bello!'
    return render_template('index.html')

@app.route('/<string:page_name>') #to dynamically plugin htm documents instead of writing multiple @app.route
# def my_website():
def html_page(page_name):
    # print(url_for('static', filename='pic.ico'))
    return render_template(page_name)

def write_to_file(data):
    with(open('database.txt', mode = 'a')) as database:
        email = data["email"]
        subject  = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with(open('database.csv', mode = 'a', newline='')) as database2:
        email = data["email"]
        subject  = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=["POST", "GET"])
def submit_form():
    # return 'form submitted hooorayyy!'
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not write to database'
    else:
        return 'something went wrong...Try again!'






# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)





# @app.route('/works.html')
# def my_home():
#     # print(url_for('static', filename='pic.ico'))
#     return render_template('works.html')

# @app.route('/about.html')
# def aboutme():
#     return render_template('about.html')
#     # 'These are my thoughts on blog post!'



# @app.route('/<username>/<int:post_id>')
# def user_world(username=None, post_id=None):
#     # print(url_for('static', filename='pic.ico'))
#     return render_template('index.html', name=username, post_id = post_id)


# # @app.route('/')
# # def blog():
# #     return render_template('index.html')
# #     # 'These are my thoughts on blog post!'

# @app.route('/aboutme')
# def aboutme():
#     return render_template('about.html')
#     # 'These are my thoughts on blog post!'

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'These are my thoughts on blog post on dogs!'

if __name__ == '__main__':
   app.run(debug=True)