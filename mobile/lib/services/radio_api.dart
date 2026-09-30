import 'dart:convert'; import 'package:http/http.dart' as http;
class RadioApi { RadioApi(this.baseUrl); final String baseUrl; Future<Map<String,dynamic>> live() async {final r=await http.get(Uri.parse('$baseUrl/api/radio/live'));if(r.statusCode!=200)throw Exception('Unable to connect to the station.');return jsonDecode(r.body);}}
