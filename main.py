from datetime import datetime

def define_env(env):

    @env.macro
    def dateformat(yyyymmdd):
        return datetime.strptime(yyyymmdd, '%Y-%m-%d').strftime("%b %d, %Y")