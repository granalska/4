import argparse
import os
import shutil
from pathlib import Path


def collect_and_copy_files(src_dir: Path, dst_dir: Path):
    """
    Рекурсивно обходить директорію src_dir, копіює файли в dst_dir,
    сортує їх по піддиректоріях за розширеннями та прибирає порожні директорії.
    """
    try:
        for root, dirs, files in os.walk(src_dir, topdown=False):

            for filename in files:
                file_path = Path(root) / filename
                ext = file_path.suffix.lower().lstrip(".") or "no_extension"
                target_folder = dst_dir / ext
                target_folder.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(file_path, target_folder)
                except Exception as e:
                    print(f"Помилка копіювання файлу {file_path}: {e}")

            #після обробки видаляємо порожню директорію
            try:
                if not os.listdir(root):
                    os.rmdir(root)
            except Exception:
                pass

    except Exception as e:
        print(f"помилка рекурсивного читання:{e}")


def main():
    parser = argparse.ArgumentParser(
        description="копія вихідної директорії, "
                    "переміщує їх у директорію призначення та сортує за розширеннями."
    )
    parser.add_argument("source", help="Шлях до вихідної директ")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Шлях до директорії призначення(за замовчуванням: dist)"
    )

    args = parser.parse_args()

    src_dir = Path(args.source).resolve()
    dst_dir = Path(args.destination).resolve()

    if not src_dir.exists() or not src_dir.is_dir():
        print("Помилка: директорія не існує")
        return

    dst_dir.mkdir(parents=True, exist_ok=True)

    collect_and_copy_files(src_dir, dst_dir)
    print(f"Копіювання та сортування у: {dst_dir}")


if __name__ == "__main__":
    main()