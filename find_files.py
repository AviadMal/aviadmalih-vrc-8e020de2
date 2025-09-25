import os


def find_files_with_extension(directory, extension):
    """
    מחזירה רשימה של קבצים בתיקייה שנמצאים עם המחזורת שניתנה, כולל בתיקיות פנימיות.
    :param directory: תיקייה להתחיל את החיפוש ממנה.
    :param extension: מחזורת הקבצים לחיפוש.
    :return: רשימה של קבצים
    """  
    matched_files = []

    # בדוק אם הקובץ הוא תיקייה
    if not os.path.isdir(directory):
        return matched_files

    # לולאת חיפוש בקבצים ובתיקיות
    for root, dirs, files in os.walk(directory):
        for file in files:
            # בודקים אם המחזורת מתאימה לקובץ הנוכחי
            if file.endswith(extension):
                matched_files.append(os.path.join(root, file))

    return matched_files


if __name__ == "__main__":
    import sys
    # בדוק את מספר הפרמטרים
    if len(sys.argv) != 3:
        print("שימוש: python find_files.py <directory> <extension>")
        sys.exit(1)

    # קרא את הפרמטרים
    directory = sys.argv[1]
    extension = sys.argv[2]

    # קרא את הקבצים
    files = find_files_with_extension(directory, extension)

    # הדפס את התוצאות
    for file in files:
        print(file)