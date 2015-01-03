from flask import Flask, render_template, request, url_for
from helpers.filters import get_browse_filters

"""
    Initialize flask APP
"""
app = Flask(__name__)


"""
    Define Routes
"""
# Home page
@app.route("/")
def homepage():
    return render_template('home.html')


# Browse GW2 Items (show results)
@app.route("/items/browse")
def gw2items_browse():
    #app.logger.debug('browse called, http method: %s' % request.method)
    
    if request.args:
        #app.logger.debug(request.args.keys())
        params = request.args
        results = True
        # @todo - load a browse model (with items collection) of the items that match the requested filters
        
    else:
        params = None
        results = False
        
    # Get filters
    filters = get_browse_filters(params)
 
    return render_template('browse.html', page='gw2items_browse', filters=filters, results=results)


# Show a specific gw2 item
@app.route("/items/view/<int:item_id>/<item_name>")
def gw2item_view():
    
    return render_template('item.html')


# Show the about page
@app.route("/about")
def about():
    return render_template('about.html', page='about')


# Test route, doesn't do much really....
@app.route('/hello/<name>/<int:post_id>')
def hello(name=None, post_id=0):
    return render_template('hello.html', name=name, post_id=post_id)



"""
    Run Application (on script run)
"""
if __name__ == "__main__":
    app.debug = True
    app.run() #host='0.0.0.0'