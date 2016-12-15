import ftplib
import os


class FTP_Connection:

    def __init__(self, host='',
                 username='anonymous',
                 password='',
                 folder='',
                 port=21):
        self.host = host
        self.username = username
        self.port = port
        self.ftp = ftplib.FTP()
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.username, password)
        if folder != '':
            self.ftp.cwd(folder)

    def cd(self, folder):
        return self.ftp.cwd(folder)

    def ls(self):
        return self.ftp.dir()

    def mkdir(self, folder):
        return self.ftp.mkd(folder)

    def upload(self, file):
        filepath = os.path.abspath(file)
        filename = os.path.split(filepath)[1]
        self.ftp.storlines("STOR " + filename, open(filepath, "rb"))

    def download(self, filename, savename=''):
        if savename == '':
            outfile = open(filename, 'wb')
        else:
            outfile = open(savename, 'wb')
        self.ftp.retrbinary("RETR " + filename, outfile.write)
