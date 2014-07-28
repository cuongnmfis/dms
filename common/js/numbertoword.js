function toWords(s) {
	//American Numbering System
	var th = ['', 'nghìn', 'triệu', 'tỷ', 'nghìn tỷ'];
	// uncomment this line for English Number System
	// var th = ['','thousand','million', 'milliard','billion'];
	
	var dg = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín'];
	var tn = ['mười', 'mười một', 'mười hai', 'mười ba', 'mười bốn', 'mười lăm', 'mười sáu', 'mười bảy', 'mười tám', 'mười chín'];
	var tw = ['hai mươi', 'ba mươi', 'bốn mươi', 'năm mươi', 'sáu mươi', 'bảy mươi', 'tám mươi', 'chín mươi'];
	s = s.toString();
	s = s.replace(/[\, ]/g, '');
	if (s != parseFloat(s))
		return 'Không phải là số';
	var x = s.indexOf('.');
	if (x == -1)
		x = s.length;
	if (x > 15)
		return 'Số quá lớn !!!';
	var n = s.split('');
	var str = '';
	var sk = 0;
	for (var i = 0; i < x; i++) {
		if ((x - i) % 3 == 2) {
			if (n[i] == '1') {
				str += tn[Number(n[i + 1])] + ' ';
				i++;
				sk = 1;
			} else if (n[i] != 0) {
				str += tw[n[i] - 2] + ' ';
				sk = 1;
			}
		} else if (n[i] != 0) {
			str += dg[n[i]] + ' ';
			if ((x - i) % 3 == 0)
				str += 'trăm ';
			sk = 1;
		}
		if ((x - i) % 3 == 1) {
			if (sk)
				str += th[(x - i - 1) / 3] + ' ';
			sk = 0;
		}
	}
	if (x != s.length) {
		var y = s.length;
		str += 'phẩy ';
		for (var i = x + 1; i < y; i++)
			str += dg[n[i]] + ' ';
	}
	return str.replace(/\s+/g, ' ');
}
