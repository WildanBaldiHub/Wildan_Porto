<?php
header('Content-Type: application/json');
// Izinkan akses dari local laptop Abang
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Content-Type");

$data = json_decode(file_get_contents('php://input'), true);

if($data) {
    $file = 'messages.json';
    
    // Ambil data lama jika ada
    if(file_exists($file)) {
        $current = json_decode(file_get_contents($file), true);
    } else {
        $current = ["inbox" => []];
    }
    
    // Tambah pesan baru
    $current['inbox'][] = [
        "sender" => $data['sender'],
        "text" => $data['text'],
        "timestamp" => date("d M Y, H:i:s"),
        "status" => "UNREAD"
    ];
    
    // Simpan kembali
    file_put_contents($file, json_encode($current, JSON_PRETTY_PRINT));
    echo json_encode(["status" => "success"]);
}
?>