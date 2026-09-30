import 'package:just_audio/just_audio.dart';
class AudioPlayerService { final player=AudioPlayer(); Future<void> playLive(String url) async {if(url.isEmpty) throw StateError('A public AzuraCast stream URL is not configured.'); await player.setUrl(url); await player.play();} Future<void> dispose()=>player.dispose(); }
