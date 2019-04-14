hellbox-fontmake
================

A hellbox job that wraps `fontmake`_ functionality in a chute.

* ``GenerateOtf`` — converts a UFO into an OTF
* ``GenerateTtf`` — converts a UFO into an TTF

.. code-block:: python

    from hellbox.job.fontmake import GenerateOtf, GenerateTtf

    with Hellbox("build") as task:
        source = task.read("*.ufo")
        source >> GenerateOtf() >> task.write("./build/otf")
        source >> GenerateTtf() >> task.write("./build/ttf")

.. _`fontmake`: https://github.com/googlei18n/fontmake

Development
-----------

.. code-block:: shell

    $ pip install -e .
    $ pytest

Contributing
------------