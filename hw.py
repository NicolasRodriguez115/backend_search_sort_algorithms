from flask import Flask, jsonify, request

app = Flask(__name__)



video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def binary_search(arr, target):
    first_index = 0 
    last_index = len(arr) - 1

    while first_index <= last_index:
        mid = (first_index + last_index) // 2
        if arr[mid] == target:
            return f'Found my target at index: {mid}'
        elif arr[mid] < target:
            first_index = mid + 1
        else:
            last_index = mid - 1
    return "Target not found"


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_side = arr[:mid]
        right_side = arr[mid:]

        merge_sort(left_side)
        merge_sort(right_side)

        m = 0
        l = 0
        r = 0

        while l < len(left_side) and r < len(right_side):
            if left_side[l].lower() < right_side[r].lower():
                arr[m] = left_side[l]
                m += 1
                l += 1
            else:
                arr[m] = right_side[r]
                m += 1
                r += 1

        while l < len(left_side):
            arr[m] = left_side[l]
            m += 1
            l += 1

        while r < len(right_side):
            arr[m] = right_side[r]
            m += 1
            r += 1

        return arr


@app.route('/search_video', methods=["GET"])
def search_video():
    video = request.args.get("video")
    result = binary_search(sorted(video_titles), video)
    return jsonify(result), 200


@app.route('/video_list', methods=["GET"])
def sort_video_list():
    result = (merge_sort(video_titles))
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)