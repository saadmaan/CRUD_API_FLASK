import argparse
from movies import *

@app.route('/movies', methods=['GET'])
def get_movies():
    '''Function to get all the movies in the database'''
    return jsonify({'Movies': Movie.get_all_movies()})

# route to get movie by id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    Movie.add_movie(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("Movie added", status = 201, mimetype='application/json')
    return response

# route to update movie with PUT method
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("Movie Updated", status=200, mimetype='application/json')
    return response

# route to delete movie using the DELETE method
@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
        help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
        help="ephemeral port number of the server (1024 to 65535)")
    args = vars(ap.parse_args())
    app.run(host=args["ip"], port=args["port"], debug=True, use_reloader=False)
#     app.run(port=8005, debug=True)