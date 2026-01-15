const mysql = require('mysql2/promise');

export default async function handler(req, res) {
    const dbConfig = {
        host: process.env.DB_HOST,
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME,
        port: 4000,
        ssl: { minVersion: 'TLSv1.2', rejectUnauthorized: true },
        connectTimeout: 10000 // Menghindari bug timeout
    };

    try {
        const db = await mysql.createConnection(dbConfig);
        
        if (req.method === 'GET') {
            const [rows] = await db.execute('SELECT * FROM projects ORDER BY id DESC');
            await db.end();
            return res.status(200).json(rows);
        }

        if (req.method === 'POST') {
            const { title, thumbnail, link, status, desc_id, desc_en, desc_jp } = req.body;
            const sql = `INSERT INTO projects (title, thumbnail, link, status, desc_id, desc_en, desc_jp) VALUES (?, ?, ?, ?, ?, ?, ?)`;
            await db.execute(sql, [title, thumbnail, link, status, desc_id, desc_en, desc_jp]);
            await db.end();
            return res.status(200).json({ success: true });
        }
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
}