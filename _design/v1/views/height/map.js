function(doc) {
  if (doc.starting_lineup) {
    var lineup = doc.starting_lineup
    for(var i=0; i<9; i++) {
      var player = lineup[i];
      emit(player.height_in_inches, doc);
    }
  }
}
