import os
import argparse
import re
import shutil

def get_args():
    parser = argparse.ArgumentParser(description="get specific domain pic")
    parser.add_argument("--folder", type=str, default="./results/maps_image_cyclegan/test_latest/images")
    parser.add_argument("--pattern", type=str, default="fake_B")
    parser.add_argument("--out_dir", type=str, default="./fake_B")

    return parser.parse_args()

def main():
    args = get_args()
    print(args)
    
    copy_count = 0
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
    for dir, dirs, files in os.walk(args.folder):
        for f in files:
            ext = f.split(".")[-1]
            if bool(re.search(args.pattern,f)):
                newname = f.split("_")[0] + "_" + f.split("_")[1] + "." +ext
                shutil.copy2(os.path.join(dir, f), os.path.join(args.out_dir, newname))
                copy_count += 1
    print(f"copy {copy_count} files to {args.out_dir}")

if __name__ == "__main__":
    main()