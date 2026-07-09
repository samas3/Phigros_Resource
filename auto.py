from androguard.misc import AnalyzeAPK
from androguard.util import set_log
import os
import shutil
import gameInformation
import getResource
from compare_file import compare_folders
from compare_meta import compare_meta, apply_diff

path = os.path.dirname(os.path.abspath(__file__))
while 'version.txt' not in os.listdir(os.path.abspath(path)):
    path = os.path.dirname(path)
version = open(os.path.join(path, 'version.txt')).read()
print('Data version: ' + version)

set_log("WARNING")
apk_path = "com.PigeonGames.Phigros.apk"
apk, _, _ = AnalyzeAPK(apk_path)
apk_version = apk.get_androidversion_name()
print('APK version: ' + apk_version)
if apk_version == version:
    print('Version match')
    exit(0)
input("Start copying data...")

config = {'UPDATE': {'main_story': 0, 'side_story': 0, 'other_song': 0}, 'avatar': False, 'Chart': True, 'IllustrationBlur': False, 'IllustrationLowRes': False, 'Illustration': True, 'music': True, 'collection': False, 'tips': False}
gameInformation.run(apk_path, config)
getResource.run(apk_path, config)

def gen_path(file_type):
    return file_type, os.path.join(path, file_type.replace('_', os.sep))

def copy_file(src, dst, diff):
    for i in diff['different'] + diff['missing']:
        file = os.path.join(src, i)
        shutil.copy(file, dst)

Chart_EZ_diff = compare_folders(*gen_path('Chart_EZ'))
print(Chart_EZ_diff)
input('Apply Chart_EZ diff...')
copy_file(*gen_path('Chart_EZ'), Chart_EZ_diff)
Chart_HD_diff = compare_folders(*gen_path('Chart_HD'))
print(Chart_HD_diff)
input('Apply Chart_HD diff...')
copy_file(*gen_path('Chart_HD'), Chart_HD_diff)
Chart_IN_diff = compare_folders(*gen_path('Chart_IN'))
print(Chart_IN_diff)
input('Apply Chart_IN diff...')
copy_file(*gen_path('Chart_IN'), Chart_IN_diff)
Chart_AT_diff = compare_folders(*gen_path('Chart_AT'))
print(Chart_AT_diff)
input('Apply Chart_AT diff...')
copy_file(*gen_path('Chart_AT'), Chart_AT_diff)

Illustration_diff = compare_folders(*gen_path('Illustration'))
print(Illustration_diff)
input('Apply Illustration diff...')
copy_file(*gen_path('Illustration'), Illustration_diff)
music_diff = compare_folders(*gen_path('music'))
print(music_diff)
input('Apply music diff...')
copy_file(*gen_path('music'), music_diff)

meta_diff = compare_meta(os.path.join(path, 'infos.csv'), 'info_new.csv')
print(meta_diff)
input('Apply meta diff...')
apply_diff(os.path.join(path, 'infos.csv'), meta_diff['diff'], meta_diff['new'])
print('View infos_new.csv to check the result.')

open(os.path.join(path, 'version.txt'), 'w').write(apk_version)