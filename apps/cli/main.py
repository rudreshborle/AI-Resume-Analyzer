--- a/apps/cli/main.py
@@ -10,7 +10,7 @@
     print("Welcome to the CLI Application")
 
 def display_header():
-    print("Header: Main Page")
+    print("\033[94mHeader: Main Page\033[0m")
 
 if __name__ == "__main__":
     main()
