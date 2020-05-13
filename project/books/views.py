# project/books/views.py

# IMPORTS
from flask import render_template, Blueprint, request, redirect, url_for, flash, Markup
from flask_login import current_user, login_required
from project import db
from project.models import Books, User
from .forms import BooksForm, EditBooksForm


# CONFIG
books_blueprint = Blueprint('books', __name__, template_folder='templates')


# ROUTES
@books_blueprint.route('/all_books', methods=['GET', 'POST'])
@login_required
def all_books():
    """Render homepage"""
    all_user_books = Books.query.filter_by(user_id=current_user.id)
    return render_template('all_books.html', books=all_user_books)


@books_blueprint.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BooksForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_book = Books(form.title.data, form.author.data, form.read_date.data, form.notes.data,
                                 current_user.id)
                db.session.add(new_book)
                db.session.commit()
                message = Markup(
                    "<strong>Well done!</strong> Book added successfully!")
                flash(message, 'success')
                return redirect(url_for('home'))
            except:
                db.session.rollback()
                message = Markup(
                    "<strong>Oh snap!</strong>! Unable to add book.")
                flash(message, 'danger')
    return render_template('add_book.html', form=form)


@books_blueprint.route('/edit_book/<books_id>', methods=['GET', 'POST'])
@login_required
def edit_book(books_id):
    form = EditBooksForm(request.form)
    book_with_user = db.session.query(Books, User).join(User).filter(Books.id == books_id).first()
    if book_with_user is not None:
        if current_user.is_authenticated and book_with_user.Books.user_id == current_user.id:
            if request.method == 'POST':
                if form.validate_on_submit():
                    try:
                        book = Books.query.get(books_id)
                        book.title = form.title.data
                        book.author = form.author.data
                        book.read_date = form.read_date.data
                        book.notes = form.notes.data
                        db.session.commit()
                        message = Markup("Book edited successfully!")
                        flash(message, 'success')
                        return redirect(url_for('home'))
                    except:
                        db.session.rollback()
                        message = Markup(
                            "<strong>Error!</strong> Unable to edit book.")
                        flash(message, 'danger')
            return render_template('edit_book.html', book=book_with_user, form=form)
        else:
            message = Markup(
                "<strong>Error!</strong> Incorrect permissions to access this book.")
            flash(message, 'danger')
    else:
        message = Markup("<strong>Error!</strong> Book does not exist.")
        flash(message, 'danger')
    return redirect(url_for('home'))


@books_blueprint.route('/delete_book/<books_id>')
@login_required
def delete_book(books_id):
    book = Books.query.filter_by(id=books_id).first_or_404()

    if not book.user_id == current_user.id:
        message = Markup(
            "<strong>Error!</strong> Incorrect permissions to delete this book.")
        flash(message, 'danger')
        return redirect(url_for('home'))

    db.session.delete(book)
    db.session.commit()
    flash('{} was deleted.'.format(book.title), 'success')
    return redirect(url_for('books.all_books'))
