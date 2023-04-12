from src.App import MainApp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = MainApp()
    app.run()
    data = app.render_geo()

    collections = app.generate_collection()


    def finder(key, value):
        return value['elevation'] == '103'


    result = collections.find(finder)
    print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
