#!/usr/bin/env python

import random
import sys


class Event(object):
    pass


class Sighting(Event):
    def __init__(self):
        self.sight = random.choice(
            ('UFO', 'bigfoot', 'ghost', 'black helicopter', 'chupacabra',
             'Yeti', 'Loch Ness monster')
        ) + ' ' + random.choice(
            ('on vacation',
             'just sitting there',
             'cheating at cards',
             'ranting obnoxiously',
             'trimming its nails',
             'looking pensive',
             'hovering overhead',
            )
        )


class ReferentialEvent(Event):
    def __init__(self):
        self.target_event = None


class Prediction(ReferentialEvent):
    pass


class Memory(ReferentialEvent):
    pass


def render_toplevel(event):
    # so much for object-orientation!
    starting_at = event
    mentioned = set([starting_at])

    (a, b) = random.choice((('Alice', 'Bob'), ('Bob', 'Alice')))

    if isinstance(event, Prediction):
        return (
            '%s turned to %s and asked, '
            '"%s, do you think that one day we will %s?"  '
            '"I don\'t know, %s," said %s.' % (
                a, b, b,
                render(event.target_event, starting_at, mentioned, tense='future'),
                a, b
            )
        )
    elif isinstance(event, Memory):
        return (
            '%s turned to %s and said, '
            '"%s, do you remember that one time when we %s?"  '
            '%s smiled.  "Of course I do, %s."' % (
                a, b, b,
                render(event.target_event, starting_at, mentioned, tense='past'),
                a, b
            )
        )
    elif isinstance(event, Sighting):
        return 'Alice and Bob saw a %s.' % event.sight
    else:
        raise NotImplementedError(event)


def render(event, starting_at, mentioned, tense='past'):
    assert event, "you should have filtered these out already you nincompoop"

    wonder = 'wondered' if tense == 'past' else 'wonder'
    remember = 'remembered' if tense == 'past' else 'remember'
    see = 'saw' if tense == 'past' else 'see'
    experience = 'experienced' if tense == 'past' else 'experience'

    # this is kind of a bodge to deal with NON-TERMINATING RECURSIVE DEJA VU
    if starting_at == event:
        return '%s this moment' % experience
    if event in mentioned:
        # hard to be more specific than this!
        return '%s that moment' % experience

    mentioned = mentioned | set([event])  # note that we do not modify the shared set

    if isinstance(event, Prediction):
        return (
            "%s if we'd ever %s" % (
                wonder,
                render(event.target_event, starting_at, mentioned, tense='future')
            )
        )
    elif isinstance(event, Memory):
        return (
            "%s that time when we %s" % (
                remember,
                render(event.target_event, starting_at, mentioned, tense='past')
            )
        )
    elif isinstance(event, Sighting):
        return "%s a %s" % (see, event.sight)
    else:
        raise NotImplementedError(event)


def main(argv):
    length = int(argv[1])

    possibilities = (
        Prediction, Prediction, Memory, Memory, Sighting
    )
    timeline = [random.choice(possibilities)() for x in xrange(0, length)]

    # FOR TESTING
    # timeline = [Prediction(), Memory()]

    while isinstance(timeline[0], Memory):
        timeline = timeline[1:]

    while isinstance(timeline[-1], Prediction):
        timeline = timeline[:-1]

    for (pos, event) in enumerate(timeline):
        event_pool = None
        if isinstance(event, Prediction):
            event_pool = timeline[pos+1:]
        elif isinstance(event, Memory):
            event_pool = timeline[:pos]
        if event_pool:
            event.target_event = random.choice(event_pool)
        else:
            #print event, pos
            pass

    # filter out unlinked events
    timeline = [t for t in timeline if isinstance(t, Sighting) or t.target_event]

    for event in timeline:
        if isinstance(event, ReferentialEvent):
            assert event.target_event, event

    for n, event in enumerate(timeline):
        x = render_toplevel(event)
        if n > 0:
            sys.stdout.write('Then one day, ')
        sys.stdout.write(x)
        sys.stdout.write('\n\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
