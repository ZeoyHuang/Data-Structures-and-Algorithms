def count_segments(segments, points):
    events = []
    for (start, end) in segments:
        events.append(('start', start))
        events.append(('end', end))
    for point in points:
        events.append(('point', point))

    # Sort events by coordinate, with a specific order for ties
    events.sort(key=lambda x: (x[1], x[0] == 'end', x[0] == 'point', x[0] == 'start'))

    segment_count = 0
    point_counts = {point: 0 for point in points}
    for event in events:
        if event[0] == 'start':
            segment_count += 1
        elif event[0] == 'end':
            segment_count -= 1
        else:  # event[0] == 'point'
            point_counts[event[1]] = segment_count

    return [point_counts[point] for point in points]

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().split())))

    points = list(map(int, input().split()))

    point_counts = count_segments(segments, points)
    for count in point_counts:
        print(count, end=' ')