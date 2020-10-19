import supervisely_lib as sly

my_app = sly.AppService()


def main():
    # Run application service
    my_app._ignore_stop_for_debug = True
    my_app.run()


if __name__ == "__main__":
    sly.main_wrapper("main", main)