import cv2 as cv
from pathlib import Path
import frames


def run(movie_path: Path, n_clusters: int):
    """

    :param movie_path:
    :param n_clusters:
    :return:
    """
    assert movie_path.is_file(), "File does not exist"
    print('Opening movie %s' % str(movie_path))
    movie = cv.VideoCapture(str(movie_path), cv.CAP_ANY)
    cluster_lst = []
    print('Analyzing frames...')
    while movie.isOpened():
        ret, frame = movie.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # cluster = frames.get_color_cluster(frame, n_clusters)
        # cluster_lst.append(cluster)
        # hist = frames.centroid_histogram(cluster)
        # bar = frames.plot_colors(hist, cluster.cluster_centers_)
        # # show our color bar
        # plt.figure()
        # plt.axis("off")
        # plt.imshow(bar)
        # plt.show()

    movie.release()
    cv.destroyAllWindows()


def run_light(movie_path: Path, n_clusters: int, skip_frames: int):
    """
    Analyze average color of each frame. Build clusters and output one screenshot each.
    :param movie_path:
    Path of the movie file
    :param n_clusters:
    number of clusters
    :param skip_frames:
    number of frames to skip, severely enhances speed
    :return:
    """
    assert movie_path.is_file(), "File does not exist"
    print('Opening movie %s' % str(movie_path))
    movie = cv.VideoCapture(str(movie_path), cv.CAP_ANY)
    color_lst = []
    print('Analyzing frames...')
    current_frame = 0
    while movie.isOpened():
        ret, frame = movie.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        avg_color = frames.get_color_avg(frame)
        color_lst.append(avg_color)
        current_frame += skip_frames + 1
        print("Current frame: %i" % current_frame)
        movie.set(cv.CAP_PROP_POS_FRAMES, current_frame - 1)
    list_cluster = frames.get_list_cluster(color_lst, n_clusters)
    frame_list = []
    print('Finding best matches...')
    for arr in list_cluster.cluster_centers_:
        lowest_dist = 1000
        frame_number = 0
        for i, color in enumerate(color_lst):
            dist = frames.array_distance(color, arr)
            if dist < lowest_dist:
                lowest_dist = dist
                frame_number = i
        frame_list.append(frame_number)
    print('Saving screenshots...')
    for image in frame_list:
        frames.save_screenshot(movie, image, skip_frames, movie_path.stem)
    movie.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    # run function here
    m_path = Path('april_story.mkv')
    run_light(m_path, 4, 59)
