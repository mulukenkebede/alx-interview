def canUnlockAll(boxes):
    # Create a set to keep track of the box indices that have been opened
    opened_boxes = {0}
    # Create a list to keep track of the keys that have been obtained
    keys = boxes[0]
    # Loop through the list of keys and boxes until no new boxes can be opened
    while True:
        # Check if all boxes have been opened
        if len(opened_boxes) == len(boxes):
            return True
        # Check if there are any new boxes that can be opened
        new_boxes = set(keys) - opened_boxes
        if not new_boxes:
            return False
        # Add the new boxes to the set of opened boxes
        opened_boxes |= new_boxes
        # Get the keys from the new boxes and add them to the list of keys
        keys = []
        for box in new_boxes:
            keys += boxes[box]
