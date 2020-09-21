var mongoose = require('mongoose');
var moment = require('moment');

var Schema = mongoose.Schema;

var AuthorSchema = new Schema(
  {
    first_name : {type: String, required: true, maxlength: 100},
    family_name : {type: String, required: true, maxlength: 100},
    date_of_birth : {type: Date},
    date_of_death : {type: Date},
  }
);

// Virtual for author's full name
AuthorSchema
.virtual('name')
.get(function() {

  // To avoid erros in cases where an author does not have either a family name of first name
  // We want to make sure we handle the exception by returning an empty string for that case

  var fullname = '';
  if (this.first_name && this.family_name) {
    fullname = this.first_name + ', ' + this.family_name;
  }
  if (!this.first_name || !this.family_name) {
    fullname = '';
  }

  return fullname;
});

// Virtual for author's lifespan
AuthorSchema
.virtual('lifespan')
.get(function() {
  return (this.date_of_death.getYear() - this.date_of_birth.getYear()).toString();
});

// Virtual for author's URL
AuthorSchema
.virtual('url')
.get(function() {
  return '/catalog/author/' + this._id;
});

// Virtual for author's date of birth
AuthorSchema
  .virtual('date_of_birth_formatted')
  .get(function() {
    return this.date_of_birth ? moment(this.date_of_birth).format('YYYY-MM-DD') : '';
  });

  // Virtual for author's date of death
  AuthorSchema
    .virtual('date_of_death_formatted')
    .get(function() {
      return this.date_of_death ? moment(this.date_of_death).format('YYYY-MM-DD') : '';
    });



// Export model
module.exports = mongoose.model('Author', AuthorSchema);