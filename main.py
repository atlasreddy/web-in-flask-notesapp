from website import create_app

app = create_app()

if __name__ == "__main__":
    # Reference Source: https://www.youtube.com/watch?v=dam0GPOAvVI
    app.run(debug=True)
