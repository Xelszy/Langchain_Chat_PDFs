# Langchain_Chat_PDFs
First Langchain Project

## Cara Kerja
---------------
Aplikasi ini mengikuti langkah-langkah berikut untuk memberikan respons terhadap pertanyaan:

1).Pemuatan PDF: Aplikasi membaca beberapa dokumen PDF dan mengekstrak konten teksnya.

2).Pembagian Teks: Teks yang diekstrak dibagi menjadi potongan-potongan kecil yang dapat diproses secara efektif.

3).Model Bahasa(LLM): Aplikasi menggunakan model bahasa untuk menghasilkan representasi vektor (embedding) dari potongan teks.

4).Pencocokan Kesamaan: Ketika pertanyaan diajukan, aplikasi membandingkannya dengan potongan-potongan teks dan mengidentifikasi yang paling serupa secara semantik.

5).Pembangkitan Respon: Potongan-potongan yang dipilih diberikan kepada model bahasa, yang menghasilkan respons berdasarkan konten relevan dari dokumen-dokumen PDF yang diberikan.
