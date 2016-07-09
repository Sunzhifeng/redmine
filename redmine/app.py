import logging

logging.basicConfig(filename='../logs/app.log',
                    level=logging.INFO)

from di import execute
from ioc import RequiredFeature, FeatureUtils
from service import UserService


class App():
    userService = RequiredFeature(UserService.__name__,
                                  FeatureUtils.isInstanceOf(UserService))

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self):
       self.userService.regist('test', 'test', False, 'test@example.com')


app = App()


if __name__ == '__main__':
    execute()
    app()
