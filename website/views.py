from website.models import Note
from flask import Blueprint, flash,request, jsonify
from flask.templating import render_template
from flask_login import login_required, current_user
from . import db
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home_view():
    print("Welcome to the site home page, ")
    if request.method == "POST":
        note = request.form.get('note')
        if len(note) < 5:
            flash("Note is too small!", category="error")
        else:
            new_note = Note(note=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added successfully", category="success")
    else:
        print("Current user notes: ",current_user.note)
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=["POST"])
@login_required
def delete_notes():
    note = json.loads(request.data)
    print("Notes deleting. ", note)

    noteId = note['noteId']
    notes = Note.query.get(noteId)
    print("Notes deleting. ", notes)

    
    if notes:
        if notes.user_id == current_user.id:
            db.session.delete(notes)
            db.session.commit()
            print("Notes deleted. ")
    return jsonify({})
