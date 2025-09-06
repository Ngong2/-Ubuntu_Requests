# Ubuntu-Inspired Image Fetcher

> *"I am because we are"* - Ubuntu Philosophy

A Python image fetcher that embodies the Ubuntu philosophy of community, respect, and sharing by connecting to the global web community to respectfully fetch and organize shared visual resources.

## 🌍 Philosophy

This project is built on the Ubuntu principles:
- **Community**: Connecting to the wider web community to access shared resources
- **Respect**: Handling errors gracefully, respecting server limits, and following web etiquette
- **Sharing**: Organizing fetched images for community appreciation and later sharing

## ✨ Features

### Core Functionality
- 🌐 **Single Image Download**: Fetch individual images from URLs
- 📦 **Batch Processing**: Download multiple images with respectful delays
- 📁 **Smart Organization**: Automatic directory creation and file management
- 🔄 **Duplicate Detection**: MD5 hash-based prevention of duplicate downloads
- 📊 **Progress Tracking**: Real-time download progress for large files

### Ubuntu-Inspired Safety & Respect
- ⚡ **Content Validation**: Checks file types and sizes before downloading
- 🛡️ **Security Measures**: Safe filename generation and content-type validation
- ⏱️ **Rate Limiting**: Respectful delays between requests to avoid overwhelming servers
- 🕵️ **Privacy Conscious**: Includes Do-Not-Track headers
- 🤝 **Proper Identification**: Uses respectful User-Agent headers

## 🚀 Quick Start

### Prerequisites
```bash
pip install requests
```

### Installation
1. Clone or download the `ubuntu_image_fetcher.py` file
2. Make it executable (Linux/Mac):
   ```bash
   chmod +x ubuntu_image_fetcher.py
   ```

### Basic Usage
```bash
python ubuntu_image_fetcher.py
```

The program will present you with an interactive menu:
1. Download single image
2. Download multiple images  
3. Use example URLs (for testing)
4. Exit

## 🧪 Testing URLs

The program includes real, working test URLs:

### HTTPBin Test Images (Reliable)
```
https://httpbin.org/image/jpeg
https://httpbin.org/image/png
https://httpbin.org/image/webp
```

### Picsum Photos (Random Images)
```
https://picsum.photos/800/600
https://picsum.photos/400/400?random=1
https://picsum.photos/1200/800?random=2
```

### Placeholder Images
```
https://via.placeholder.com/500x300.jpg
https://via.placeholder.com/600x400.png
```

## 📚 Usage Examples

### Single Image Download
```python
from ubuntu_image_fetcher import UbuntuImageFetcher

fetcher = UbuntuImageFetcher()
fetcher.fetch_image("https://httpbin.org/image/jpeg")
```

### Multiple Images with Custom Delay
```python
urls = [
    "https://httpbin.org/image/jpeg",
    "https://picsum.photos/800/600",
    "https://via.placeholder.com/500x300.jpg"
]

fetcher.fetch_multiple_images(urls, delay=2)  # 2-second delay between requests
```

## 🗂️ File Organization

Images are saved to the `Fetched_Images/` directory with:
- Smart filename extraction from URLs
- Fallback hash-based naming for complex URLs
- Automatic duplicate numbering for conflicts
- Safe filesystem-compatible names

## 🔒 Security Features

### Content Validation
- **Safe File Types**: Only allows common image formats (JPEG, PNG, GIF, WebP, BMP, TIFF, SVG)
- **Size Limits**: Maximum 50MB per file to prevent abuse
- **Content-Type Checking**: Validates HTTP headers before download

### Network Safety
- **Timeout Handling**: 30-second request timeouts
- **Error Recovery**: Graceful handling of network failures
- **Rate Limiting**: Configurable delays between requests

## 🛠️ Advanced Features

### Duplicate Prevention
The fetcher maintains MD5 hashes of all downloaded files to prevent duplicates:
```python
# Automatically detects and skips duplicate content
✅ New image: saved as image_abc123.jpg
⚠️  Duplicate image detected - Ubuntu wisdom: sharing without waste
```

### Progress Tracking
For large files, real-time progress updates:
```
📊 Progress: 25.3%
📊 Progress: 50.7%
📊 Progress: 75.1%
✅ Successfully saved: large_image.jpg
```

### HTTP Headers Inspection
Before downloading, the program checks:
- `Content-Type`: Ensures it's a valid image format
- `Content-Length`: Validates file size limits
- Response codes and redirects

## 🎯 Assignment Requirements Met

### ✅ Core Requirements
- [x] Uses `requests` library for fetching
- [x] Handles HTTP errors appropriately
- [x] Creates directory with `os.makedirs(exist_ok=True)`
- [x] Extracts/generates appropriate filenames
- [x] Saves images in binary mode
- [x] Implements Ubuntu principles throughout

### ✅ Challenge Features
- [x] **Multiple URL Support**: Batch processing with queue management
- [x] **Security Precautions**: Content validation, size limits, safe naming
- [x] **Duplicate Prevention**: MD5 hash-based detection system  
- [x] **HTTP Header Analysis**: Content-Type and Content-Length validation

## 🐛 Error Handling

The program gracefully handles:
- **Network Issues**: Connection timeouts, DNS failures
- **HTTP Errors**: 404 Not Found, 403 Forbidden, 500 Server Error
- **File System Issues**: Permission errors, disk space
- **Content Issues**: Invalid image types, oversized files

Example error messages:
```
🔌 Connection failed - server may be unavailable
⏱️  Connection timed out - respecting server limits
🌐 HTTP error 404: Not Found
✗ Unsafe content type: text/html
✗ File too large: 52,428,800 bytes
```

## 📊 Ubuntu Summary Report

After batch processing, you'll see a community-focused summary:
```
📊 Ubuntu Summary:
✅ Successful: 4
❌ Failed: 1  
📁 Images stored in: Fetched_Images
🤝 Ubuntu wisdom: 'I am because we are' - Connected to 4 community resources
```

## 🤝 Contributing

In the spirit of Ubuntu, contributions are welcome! Please:
1. Maintain the philosophy of respect and community
2. Add comprehensive error handling
3. Include tests for new features
4. Update documentation

## 📄 License

This project embodies the Ubuntu philosophy of sharing and community. Use it respectfully and share your improvements with others.

## 🙏 Acknowledgments

- Built on the Ubuntu philosophy: *"A person is a person through other persons"*
- Thanks to the global web community for sharing visual resources
- Inspired by the principles of respectful web citizenship

---

*"Ubuntu: I am what I am because of who we all are."* - Archbishop Desmond Tutu
