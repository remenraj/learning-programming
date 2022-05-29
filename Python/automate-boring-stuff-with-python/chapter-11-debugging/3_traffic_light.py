# Traffic light
# example program for asserting and debugging

def switch_lights(intersection):
    for light in intersection:
        if light == "green":
            intersection[light] = "yellow"
        elif light == "yellow":
            intersection[light] = "red"
        elif light == "red":
            intersection[light] = "green"
    
    assert "red" in intersection.values(), "Neither light is red!" + str(intersection)


if __name__ == "__main__":
    market_2nd = {
        "ns": "green",
        "ew": "red"
    }
    switch_lights(intersection=market_2nd)
    