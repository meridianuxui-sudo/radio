import 'package:flutter_test/flutter_test.dart';
import 'package:meradion/main.dart';
void main(){testWidgets('home identifies MeradioN', (tester) async {await tester.pumpWidget(const MeradionApp());expect(find.text("Meradio'N"), findsOneWidget);});}
