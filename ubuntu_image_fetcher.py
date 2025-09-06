#!/usr/bin/env python3
"""
Ubuntu-Inspired Image Fetcher
"I am because we are" - Ubuntu Philosophy

This script embodies Ubuntu principles by respectfully connecting to the global
web community to fetch and organize shared visual resources.
"""

import os
import requests
import hashlib
import mimetypes
from urllib.parse import urlparse, unquote
from pathlib import Path
import time

class UbuntuImageFetcher:
    """
    A respectful image fetcher that embodies Ubuntu principles:
    - Community: Connects to the global web community
    - Respect: Handles errors gracefully and follows web etiquette
    - Sharing: Organizes images for community sharing
    """
    
    def __init__(self, download_dir="Fetched_Images"):
        self.download_dir = Path(download_dir)
        self.downloaded_hashes = set()
        self.session = requests.Session()
        
        # Set respectful headers following Ubuntu principle of respect
        self.session.headers.update({
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Educational Purpose; Respectful Web Citizen)',
            'Accept': 'image/*,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'DNT': '1'  # Do Not Track - respecting privacy
        })
        
        # Create directory following Ubuntu principle of preparation
        self.ensure_directory_exists()
        self.load_existing_hashes()
    
    def ensure_directory_exists(self):
        """Create the download directory if it doesn't exist - Ubuntu: Practical action"""
        try:
            self.download_dir.mkdir(parents=True, exist_ok=True)
            print(f"✓ Directory '{self.download_dir}' ready for community sharing")
        except Exception as e:
            print(f"✗ Could not create directory: {e}")
            raise
    
    def load_existing_hashes(self):
        """Load hashes of existing files to prevent duplicates - Ubuntu: Efficiency"""
        for file_path in self.download_dir.glob("*"):
            if file_path.is_file():
                try:
                    with open(file_path, 'rb') as f:
                        file_hash = hashlib.md5(f.read()).hexdigest()
                        self.downloaded_hashes.add(file_hash)
                except Exception:
                    continue  # Skip files we can't read
    
    def is_safe_content_type(self, content_type):
        """Check if content type is a safe image format - Ubuntu: Respect & Safety"""
        safe_types = {
            'image/jpeg', 'image/jpg', 'image/png', 'image/gif', 
            'image/webp', 'image/bmp', 'image/tiff', 'image/svg+xml'
        }
        return content_type.lower().split(';')[0] in safe_types
    
    def generate_filename(self, url, content_type=None, content=None):
        """Generate appropriate filename - Ubuntu: Practical organization"""
        # Try to extract filename from URL
        parsed_url = urlparse(url)
        path = unquote(parsed_url.path)
        
        if path and '.' in os.path.basename(path):
            filename = os.path.basename(path)
        else:
            # Generate filename from URL hash and content type
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            
            # Determine extension from content type
            extension = '.jpg'  # default
            if content_type:
                extension = mimetypes.guess_extension(content_type.split(';')[0]) or '.jpg'
            
            filename = f"image_{url_hash}{extension}"
        
        # Ensure filename is safe for filesystem
        filename = "".join(c for c in filename if c.isalnum() or c in "._-")
        
        # Handle duplicates by adding counter
        base_path = self.download_dir / filename
        counter = 1
        while base_path.exists():
            name, ext = os.path.splitext(filename)
            base_path = self.download_dir / f"{name}_{counter}{ext}"
            counter += 1
        
        return base_path.name
    
    def fetch_image(self, url, timeout=30):
        """
        Fetch a single image with Ubuntu principles:
        - Respect: Proper error handling and timeouts
        - Community: Connecting to shared resources
        """
        print(f"\n🌍 Connecting to community resource: {url}")
        
        try:
            # Make HEAD request first to check content - Ubuntu: Respect
            head_response = self.session.head(url, timeout=timeout, allow_redirects=True)
            
            # Check important headers
            content_type = head_response.headers.get('Content-Type', '')
            content_length = head_response.headers.get('Content-Length')
            
            if not self.is_safe_content_type(content_type):
                print(f"✗ Unsafe content type: {content_type}")
                return False
            
            # Check file size (limit to 50MB for safety)
            if content_length and int(content_length) > 50 * 1024 * 1024:
                print(f"✗ File too large: {content_length} bytes")
                return False
            
            print(f"📋 Content-Type: {content_type}")
            if content_length:
                print(f"📏 Content-Length: {int(content_length):,} bytes")
            
            # Now fetch the actual image
            print("⬇️  Downloading image...")
            response = self.session.get(url, timeout=timeout, stream=True)
            response.raise_for_status()
            
            # Read content and check for duplicates
            content = b''
            downloaded_size = 0
            
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    content += chunk
                    downloaded_size += len(chunk)
                    
                    # Progress indicator for large files
                    if content_length and downloaded_size % (1024 * 1024) == 0:
                        progress = (downloaded_size / int(content_length)) * 100
                        print(f"📊 Progress: {progress:.1f}%")
            
            # Check for duplicate using hash - Ubuntu: Efficiency
            content_hash = hashlib.md5(content).hexdigest()
            if content_hash in self.downloaded_hashes:
                print("⚠️  Duplicate image detected - Ubuntu wisdom: sharing without waste")
                return False
            
            # Generate filename and save
            filename = self.generate_filename(url, content_type, content)
            file_path = self.download_dir / filename
            
            with open(file_path, 'wb') as f:
                f.write(content)
            
            self.downloaded_hashes.add(content_hash)
            
            print(f"✅ Successfully saved: {filename}")
            print(f"📁 Location: {file_path}")
            print(f"📊 Size: {len(content):,} bytes")
            
            return True
            
        except requests.exceptions.Timeout:
            print("⏱️  Connection timed out - respecting server limits")
            return False
        except requests.exceptions.ConnectionError:
            print("🔌 Connection failed - server may be unavailable")
            return False
        except requests.exceptions.HTTPError as e:
            print(f"🌐 HTTP error {e.response.status_code}: {e.response.reason}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"📡 Request failed: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False
    
    def fetch_multiple_images(self, urls, delay=1):
        """
        Fetch multiple images with Ubuntu respect:
        - Community: Batch processing for efficiency
        - Respect: Delays between requests to not overwhelm servers
        """
        print(f"\n🎯 Processing {len(urls)} URLs with Ubuntu respect...")
        
        successful = 0
        failed = 0
        
        for i, url in enumerate(urls, 1):
            print(f"\n--- Image {i}/{len(urls)} ---")
            
            if self.fetch_image(url.strip()):
                successful += 1
            else:
                failed += 1
            
            # Respectful delay between requests - Ubuntu: Respect
            if i < len(urls):
                print(f"⏸️  Respectful pause ({delay}s)...")
                time.sleep(delay)
        
        print(f"\n📊 Ubuntu Summary:")
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📁 Images stored in: {self.download_dir}")
        print(f"🤝 Ubuntu wisdom: 'I am because we are' - Connected to {successful} community resources")

def main():
    """Main function demonstrating Ubuntu principles in action"""
    print("🌍 Ubuntu Image Fetcher - 'I am because we are'")
    print("=" * 50)
    
    fetcher = UbuntuImageFetcher()
    
    # Provide real example URLs for testing
    example_urls = [
        "https://httpbin.org/image/jpeg",  # Test JPEG image
        "https://httpbin.org/image/png",   # Test PNG image
        "https://httpbin.org/image/webp",  # Test WebP image
        "https://picsum.photos/800/600",   # Random landscape image
        "https://picsum.photos/400/400?random=1",  # Random square image
    ]
    
    print("\n🎯 Example URLs you can test:")
    for i, url in enumerate(example_urls, 1):
        print(f"{i}. {url}")
    
    print("\n" + "─" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Download single image")
        print("2. Download multiple images")
        print("3. Use example URLs")
        print("4. Exit")
        
        choice = input("\nYour choice (1-4): ").strip()
        
        if choice == '1':
            url = input("Enter image URL: ").strip()
            if url:
                fetcher.fetch_image(url)
            else:
                print("No URL provided")
        
        elif choice == '2':
            print("Enter multiple URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                delay = input("Delay between requests in seconds (default 1): ").strip()
                try:
                    delay = float(delay) if delay else 1
                except ValueError:
                    delay = 1
                fetcher.fetch_multiple_images(urls, delay)
            else:
                print("No URLs provided")
        
        elif choice == '3':
            print("\n🧪 Testing with example URLs...")
            fetcher.fetch_multiple_images(example_urls, delay=0.5)
        
        elif choice == '4':
            print("\n🤝 Ubuntu farewell: May your images bring community joy!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()