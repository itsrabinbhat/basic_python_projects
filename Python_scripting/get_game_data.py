import os
import sys
import json
import shutil
from subprocess import run, PIPE

GAME_DIR_PATTERN = "game"
GAME_CODE_EXT = ".go"
GAME_COMPILE_CMDS = ["go", "build"]


# get paths of all the dirs with "game" in their name
def get_paths(source):
    game_paths = []
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        break

    return game_paths


# get directory names from game_paths
def get_dir_names(paths, to_strip):
    dir_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        dir_names.append(new_dir_name)

    return dir_names


# copy and overwrite the files to target dir
def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)


# create target directory
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# create and store info in json file
def create_json_metadata_file(path, dirs_names):
    data = {"gameNames": dirs_names, "noOfGames": len(dirs_names)}
    with open(path, "w") as f:
        json.dump(data, f)


def run_cmds(cmds, path):
    cwd = os.getcwd()
    os.chdir(path)
    # print(cmds)
    result = run(cmds, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("Compile result: ", result)
    os.chdir(cwd)


# compile game code
def compile_code(path):
    code_file = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXT):
                code_file = file
                break
        break
    if code_file is None:
        return

    cmds = GAME_COMPILE_CMDS + [code_file]
    run_cmds(cmds, path)


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = get_paths(source_path)
    dir_names = get_dir_names(game_paths, "_game")

    for src, dest in zip(game_paths, dir_names):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_code(dest_path)

    create_dir(target_path)

    json_path = os.path.join(target_path, "metadata.json")

    create_json_metadata_file(json_path, dir_names)


# get args from cmd line
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass Source & Target Only!")
    source, target = args[1:]
    main(source, target)
