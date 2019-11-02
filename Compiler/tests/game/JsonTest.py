from game.Balloons import Balloons
from game.CobWeb import CobWeb, Card
from game.Game import Game
from game.Piano import Piano
from game.Targets import Targets

ok = "OK"


# Main function to run the test
def encoding_test():
    print("\nGame_Encoding_TEST running... ")

    piano_test()
    targets_test()
    balloons_test()
    cob_web_test()

    print(ok)


def piano_test():
    print("\tPiano_TEST running... ", end='')
    json = "{\"colors\":[\"red\",\"blue\",\"green\",\"yellow\"],\"points\":[1,2,3,4],\"time\":60}"
    piano = Piano(["red", "blue", "green", "yellow"],
                  [1, 2, 3, 4],
                  60).to_json()

    if json.__eq__(piano.replace(' ', '')):
        print(ok)
    else:
        exit(1)


def targets_test():
    print("\tTargets_TEST running... ", end='')
    json = "{\"x\":5,\"y\":6,\"time\":30}"
    targets = Targets(5, 6, 30).to_json()

    if json.__eq__(targets.replace(' ', '')):
        print(ok)
    else:
        exit(1)


def balloons_test():
    print("\tBalloons_TEST running... ", end='')
    json = "{\"x\":5,\"y\":6}"
    balloons = Balloons(5, 6).to_json()

    if json.__eq__(balloons.replace(' ', '')):
        print(ok)
    else:
        exit(1)


def cob_web_test():
    print("\tCobWeb_TEST running... ", end='')
    json = "{\"cards\":[{\"name\":\"ocean\",\"points\":10,\"i\":0,\"j\":0},{\"name\":\"sky\",\"points\":5,\"i\":0," \
           "\"j\":1},{\"name\":\"river\",\"points\":4,\"i\":1,\"j\":0},{\"name\":\"mountain\",\"points\":8,\"i\":1," \
           "\"j\":1}]}"
    cob_web = CobWeb([Card("ocean", 10, 0, 0).dict(),
                     Card("sky", 5, 0, 1).dict(),
                     Card("river", 4, 1, 0).dict(),
                     Card("mountain", 8, 1, 1).dict()
                      ]).to_json()

    if json.__eq__(cob_web.replace(' ', '')):
        print(ok)
    else:
        exit(1)
