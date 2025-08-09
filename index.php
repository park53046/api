<?php
header('Content-Type: application/json; charset=utf-8');

$render_base = 'https://park5300-fastapi.onrender.com'; // Render 주소로 교체
$req_uri = $_SERVER['REQUEST_URI']; // 예: /api/me
$path = preg_replace('#^/api#', '', $req_uri); // /me

$ch = curl_init($render_base.$path.($_SERVER['QUERY_STRING'] ? '?'.$_SERVER['QUERY_STRING'] : ''));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept: application/json']);
$resp = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

http_response_code($code ?: 200);
echo $resp;
