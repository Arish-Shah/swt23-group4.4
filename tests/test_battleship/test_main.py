from battleship.__main__ import main

def test_main(mocker):
    mock_play = mocker.patch("battleship.game.Game.play")
    main()
    assert mock_play.called
