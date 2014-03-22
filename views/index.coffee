cradle = require 'cradle'
db = new(cradle.Connection)().database('v1')

handler = (err, res) ->
  console.log err
  console.log res

body =
  views:
    height:
      map: (doc) ->
        if doc.starting_lineup
          for player in doc.starting_lineup
            emit(player.height_in_inches, doc)

db.save '_design/games', body, handler


