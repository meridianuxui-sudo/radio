import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
void main()=>runApp(const MeradionApp());
class MeradionApp extends StatelessWidget {const MeradionApp({super.key}); @override Widget build(BuildContext context)=>MaterialApp(title:"Meradio'N",debugShowCheckedModeBanner:false,theme:ThemeData(useMaterial3:true,colorScheme:ColorScheme.fromSeed(seedColor:const Color(0xff556b2f),brightness:Brightness.light),scaffoldBackgroundColor:const Color(0xfff5eedc),fontFamily:'sans'),home:const HomeScreen());}
