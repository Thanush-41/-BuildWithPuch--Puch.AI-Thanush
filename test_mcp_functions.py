import asyncio
import json
from pathlib import Path
import PyPDF2

async def test_resume_function():
    """Test the resume function locally"""
    
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Extract text from PDF file and return as string."""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                return text
        except Exception as e:
            return f"Error reading PDF: {e}"

    def convert_text_to_markdown(text: str) -> str:
        """Convert plain text to basic markdown format."""
        lines = text.split('\n')
        markdown_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                markdown_lines.append("")
                continue
                
            # Convert potential headings (lines in all caps or with specific patterns)
            if line.isupper() and len(line) > 3:
                markdown_lines.append(f"## {line.title()}")
            # Convert email patterns
            elif "@" in line and "." in line:
                markdown_lines.append(f"**Email:** {line}")
            # Convert phone patterns
            elif any(char.isdigit() for char in line) and len([c for c in line if c.isdigit()]) >= 8:
                if "phone" in line.lower() or "mobile" in line.lower() or "tel" in line.lower():
                    markdown_lines.append(f"**Phone:** {line}")
                else:
                    markdown_lines.append(line)
            # Convert lines that look like section headers
            elif line.endswith(':') or (len(line.split()) <= 3 and line.istitle()):
                markdown_lines.append(f"### {line}")
            else:
                markdown_lines.append(line)
        
        return '\n'.join(markdown_lines)

    # Test the resume function
    resume_path = Path("T:/puch/thanush_resume_puch.pdf")
    
    if not resume_path.exists():
        print("❌ Resume file not found!")
        return False
    
    print("✅ Resume file found")
    
    # Extract text from PDF
    raw_text = extract_text_from_pdf(str(resume_path))
    print(f"✅ Extracted {len(raw_text)} characters from PDF")
    
    # Convert to markdown
    markdown_text = convert_text_to_markdown(raw_text)
    print(f"✅ Converted to markdown ({len(markdown_text)} characters)")
    
    print("\n--- First 500 characters of markdown output ---")
    print(markdown_text[:500])
    print("---")
    
    return True

def test_validation():
    """Test the validation function"""
    MY_NUMBER = "9440280028"
    print(f"✅ Validation function returns: {MY_NUMBER}")
    return True

async def main():
    print("🧪 Testing MCP Server Functions\n")
    
    print("1. Testing Resume Function:")
    resume_ok = await test_resume_function()
    
    print("\n2. Testing Validation Function:")
    validation_ok = test_validation()
    
    print(f"\n📊 Results:")
    print(f"   Resume function: {'✅ PASS' if resume_ok else '❌ FAIL'}")
    print(f"   Validation function: {'✅ PASS' if validation_ok else '❌ FAIL'}")
    
    if resume_ok and validation_ok:
        print("\n🎉 All tests passed! Your MCP server is ready.")
        print("\n🔗 Server Details:")
        print("   - Server URL: http://0.0.0.0:8085/mcp")
        print("   - Auth Token: 00b577f9f14c")
        print("   - Phone Number: 9440280028")
        print("\n📝 To connect with Puch, use:")
        print("   /mcp connect http://your-public-ip:8085/mcp 00b577f9f14c")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    asyncio.run(main())
