 source/backend/apache2-config/000-default.conf
@@ -0,0 +1,12 @@
+<VirtualHost *>
+    ServerName example.com
+
+    WSGIDaemonProcess seefood user=www-server group=www-server threads=5
+    WSGIScriptAlias / /var/www/seefood/seefood.wsgi
+
+    <Directory /var/www/seefood>
+        WSGIProcessGroup seefood
+        WSGIApplicationGroup %{GLOBAL}
+        Require all granted
+    </Directory>
+</VirtualHost>

+from flask import Flask
+app = Flask(__name__)
+
+
+@app.route("/")
+def hello():
+    return "Hello World!"

+import os
+import sys
+
+sys.path.insert(0, "/var/www/seefood/")
+
+from application import app as application


+<VirtualHost *>
+    ServerName example.com
+
+    WSGIDaemonProcess seefood user=www-server group=www-server threads=5
+    WSGIScriptAlias / /var/www/seefood/seefood.wsgi
+
+    <Directory /var/www/seefood>
+        WSGIProcessGroup seefood
+        WSGIApplicationGroup %{GLOBAL}
+        Require all granted
+    </Directory>
+</VirtualHost>

+<?xml version="1.0" encoding="UTF-8"?>
+<module type="PYTHON_MODULE" version="4">
+  <component name="NewModuleRootManager">
+    <content url="file://$MODULE_DIR$" />
+    <orderEntry type="jdk" jdkName="Python 2.7.10 (/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7)" jdkType="Python SDK" />
+    <orderEntry type="sourceFolder" forTests="false" />
+  </component>
+  <component name="TestRunnerService">
+    <option name="PROJECT_TEST_RUNNER" value="Unittests" />
+  </component>
+</module> 


+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="ProjectRootManager" version="2" project-jdk-name="Python 2.7.10 (/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7)" project-jdk-type="Python SDK" />
+</project> 


+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="ProjectModuleManager">
+    <modules>
+      <module fileurl="file://$PROJECT_DIR$/.idea/CEG4100-SeeFood.iml" filepath="$PROJECT_DIR$/.idea/CEG4100-SeeFood.iml" />
+    </modules>
+  </component>
+</project> 



+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="VcsDirectoryMappings">
+    <mapping directory="$PROJECT_DIR$" vcs="Git" />
+  </component>
+</project> 
+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="ChangeListManager">
+    <list default="true" id="2c32c9ee-8d93-45b8-8d94-d41f0ecabd8a" name="Default" comment="">
+      <change type="NEW" beforePath="" afterPath="$PROJECT_DIR$/.idea/vcs.xml" />
+      <change type="MODIFICATION" beforePath="$PROJECT_DIR$/source/backend/application.py" afterPath="$PROJECT_DIR$/source/backend/application.py" />
+    </list>
+    <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />
+    <option name="TRACKING_ENABLED" value="true" />
+    <option name="SHOW_DIALOG" value="false" />
+    <option name="HIGHLIGHT_CONFLICTS" value="true" />
+    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
+    <option name="LAST_RESOLUTION" value="IGNORE" />
+  </component>
+  <component name="FileEditorManager">
+    <leaf SIDE_TABS_SIZE_LIMIT_KEY="300">
+      <file leaf-file-name="application.py" pinned="false" current-in-tab="true">
+        <entry file="file://$PROJECT_DIR$/source/backend/application.py">
+          <provider selected="true" editor-type-id="text-editor">
+            <state relative-caret-position="195">
+              <caret line="13" column="25" lean-forward="true" selection-start-line="13" selection-start-column="25" selection-end-line="13" selection-end-column="25" />
+              <folding />
+            </state>
+          </provider>
+        </entry>
+      </file>
+    </leaf>
+  </component>
+  <component name="Git.Settings">
+    <option name="RECENT_GIT_ROOT_PATH" value="$PROJECT_DIR$" />
+  </component>
+  <component name="IdeDocumentHistory">
+    <option name="CHANGED_PATHS">
+      <list>
+        <option value="$PROJECT_DIR$/source/backend/application.py" />
+      </list>
+    </option>
+  </component>
+  <component name="ProjectFrameBounds">
+    <option name="y" value="23" />
+    <option name="width" value="1440" />
+    <option name="height" value="783" />
+  </component>
+  <component name="ProjectLevelVcsManager">
+    <ConfirmationsSetting value="2" id="Add" />
+  </component>
+  <component name="ProjectView">
+    <navigator currentView="ProjectPane" proportions="" version="1">
+      <flattenPackages />
+      <showMembers />
+      <showModules />
+      <showLibraryContents />
+      <hideEmptyPackages />
+      <abbreviatePackageNames />
+      <autoscrollToSource />
+      <autoscrollFromSource />
+      <sortByType />
+      <manualOrder />
+      <foldersAlwaysOnTop value="true" />
+    </navigator>
+    <panes>
+      <pane id="Scratches" />
+      <pane id="Scope" />
+      <pane id="ProjectPane">
+        <subPane>
+          <expand>
+            <path>
+              <item name="CEG4100-SeeFood" type="b2602c69:ProjectViewProjectNode" />
+              <item name="CEG4100-SeeFood" type="462c0819:PsiDirectoryNode" />
+            </path>
+            <path>
+              <item name="CEG4100-SeeFood" type="b2602c69:ProjectViewProjectNode" />
+              <item name="CEG4100-SeeFood" type="462c0819:PsiDirectoryNode" />
+              <item name="source" type="462c0819:PsiDirectoryNode" />
+            </path>
+            <path>
+              <item name="CEG4100-SeeFood" type="b2602c69:ProjectViewProjectNode" />
+              <item name="CEG4100-SeeFood" type="462c0819:PsiDirectoryNode" />
+              <item name="source" type="462c0819:PsiDirectoryNode" />
+              <item name="backend" type="462c0819:PsiDirectoryNode" />
+            </path>
+          </expand>
+          <select />
+        </subPane>
+      </pane>
+    </panes>
+  </component>
+  <component name="PropertiesComponent">
+    <property name="last_opened_file_path" value="$PROJECT_DIR$" />
+    <property name="settings.editor.selected.configurable" value="com.jetbrains.python.configuration.PyActiveSdkModuleConfigurable" />
+  </component>
+  <component name="RunDashboard">
+    <option name="ruleStates">
+      <list>
+        <RuleState>
+          <option name="name" value="ConfigurationTypeDashboardGroupingRule" />
+        </RuleState>
+        <RuleState>
+          <option name="name" value="StatusDashboardGroupingRule" />
+        </RuleState>
+      </list>
+    </option>
+  </component>
+  <component name="RunManager" selected="Python.application">
+    <configuration name="application" type="PythonConfigurationType" factoryName="Python" singleton="true">
+      <option name="INTERPRETER_OPTIONS" value="" />
+      <option name="PARENT_ENVS" value="true" />
+      <envs>
+        <env name="PYTHONUNBUFFERED" value="1" />
+      </envs>
+      <option name="SDK_HOME" value="" />
+      <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$/source/backend" />
+      <option name="IS_MODULE_SDK" value="true" />
+      <option name="ADD_CONTENT_ROOTS" value="true" />
+      <option name="ADD_SOURCE_ROOTS" value="true" />
+      <module name="CEG4100-SeeFood" />
+      <option name="SCRIPT_NAME" value="$PROJECT_DIR$/source/backend/application.py" />
+      <option name="PARAMETERS" value="" />
+      <option name="SHOW_COMMAND_LINE" value="false" />
+      <option name="EMULATE_TERMINAL" value="false" />
+    </configuration>
+  </component>
+  <component name="ShelveChangesManager" show_recycled="false">
+    <option name="remove_strategy" value="false" />
+  </component>
+  <component name="TaskManager">
+    <task active="true" id="Default" summary="Default task">
+      <changelist id="2c32c9ee-8d93-45b8-8d94-d41f0ecabd8a" name="Default" comment="" />
+      <created>1507653539430</created>
+      <option name="number" value="Default" />
+      <option name="presentableId" value="Default" />
+      <updated>1507653539430</updated>
+    </task>
+    <servers />
+  </component>
+  <component name="ToolWindowManager">
+    <frame x="0" y="23" width="1440" height="783" extended-state="0" />
+    <layout>
+      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="0" side_tool="false" content_ui="combo" />
+      <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />
+      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="true" content_ui="tabs" />
+      <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
+      <window_info id="Python Console" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
+      <window_info id="Run" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32911393" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />
+      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
+      <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />
+      <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="true" content_ui="tabs" />
+      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
+      <window_info id="Data View" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />
+      <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />
+      <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
+      <window_info id="Commander" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="0" side_tool="false" content_ui="tabs" />
+      <window_info id="Inspection" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="5" side_tool="false" content_ui="tabs" />
+      <window_info id="Hierarchy" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="combo" />
+      <window_info id="Find" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
+      <window_info id="Ant Build" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />
+    </layout>
+  </component>
+  <component name="VcsContentAnnotationSettings">
+    <option name="myLimit" value="2678400000" />
+  </component>
+  <component name="XDebuggerManager">
+    <breakpoint-manager />
+    <watches-manager />
+  </component>
+  <component name="editorHistoryManager">
+    <entry file="file://$PROJECT_DIR$/source/backend/application.py">
+      <provider selected="true" editor-type-id="text-editor">
+        <state relative-caret-position="0">
+          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
+          <folding />
+        </state>
+      </provider>
+    </entry>
+    <entry file="file://$PROJECT_DIR$/source/backend/__init__.py">
+      <provider selected="true" editor-type-id="text-editor">
+        <state relative-caret-position="0">
+          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />
+        </state>
+      </provider>
+    </entry>
+    <entry file="file://$PROJECT_DIR$/source/backend/application.py">
+      <provider selected="true" editor-type-id="text-editor">
+        <state relative-caret-position="195">
+          <caret line="13" column="25" lean-forward="true" selection-start-line="13" selection-start-column="25" selection-end-line="13" selection-end-column="25" />
+          <folding />
+        </state>
+      </provider>
+    </entry>
+  </component>
+</project> 



source/backend/apache2-config/000-default.conf

+<VirtualHost *>
+    ServerName example.com
+
+    WSGIDaemonProcess seefood user=www-server group=www-server threads=5
+    WSGIScriptAlias / /var/www/seefood/seefood.wsgi
+
+    <Directory /var/www/seefood>
+        WSGIProcessGroup seefood
+        WSGIApplicationGroup %{GLOBAL}
+        Require all granted
+    </Directory>
+</VirtualHost>



source/backend/application.py
+from flask import Flask
+app = Flask(__name__)
+
+
+@app.route("/")
+def hello():
+    return "Hello World!"

source/backend/seefood.wsgi
+import os
+import sys
+
+sys.path.insert(0, "/var/www/seefood/")
+
+from application import app as application





 .idea/CEG4100-SeeFood.iml
+<?xml version="1.0" encoding="UTF-8"?>
+<module type="PYTHON_MODULE" version="4">
+  <component name="NewModuleRootManager">
+    <content url="file://$MODULE_DIR$" />
+    <orderEntry type="jdk" jdkName="Python 2.7.10 (/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7)" jdkType="Python SDK" />
+    <orderEntry type="sourceFolder" forTests="false" />
+  </component>
+  <component name="TestRunnerService">
+    <option name="PROJECT_TEST_RUNNER" value="Unittests" />
+  </component>
+</module> 


 .idea/misc.xml
+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="ProjectRootManager" version="2" project-jdk-name="Python 2.7.10 (/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7)" project-jdk-type="Python SDK" />
+</project> 


 .idea/modules.xml

+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="ProjectModuleManager">
+    <modules>
+      <module fileurl="file://$PROJECT_DIR$/.idea/CEG4100-SeeFood.iml" filepath="$PROJECT_DIR$/.idea/CEG4100-SeeFood.iml" />
+    </modules>
+  </component>
+</project> 


idea/vcs.xml

+<?xml version="1.0" encoding="UTF-8"?>
+<project version="4">
+  <component name="VcsDirectoryMappings">
+    <mapping directory="$PROJECT_DIR$" vcs="Git" />
+  </component>
+</project> 


000-default.conf

<VirtualHost *>000-default.conf

    ServerName example.com

    WSGIDaemonProcess seefood user=www-server group=www-server threads=5
    WSGIScriptAlias / /var/www/fooddroid/fooddroid.wsgi

    <Directory /var/www/fooddroid>
        WSGIProcessGroup fooddroid
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
</VirtualHost>



FORMAT: 1A
HOST: http://amazon-ec2-instance-ip/

# seefood-ai

seefood-ai is a simple REST API that interfaces with the Seefood AI in the cloud to 
analyze images and whether or not they contain food.

## Gallery Management [/gallery]
### Receive Gallery [GET]

Request a list of images that have been uploaded to the server, 
limited to a specific number of results.

+ Request (application/json)

        {
            "page": 1,
            "limit": 20
        }

+ Response 200 (application/json)

        [
            {
                "name": "wooden_table",
                "type": "png",
                "data": "AB00234AFDFDAD2002340F0011000000100100011AE324FFAD32...",
                "uploaded_at": "2015-08-05T08:40:51.620Z",
                "contains_food": "No",
                "certainty": .9
            },
            {
                "name": "apple",
                "type": "png",
                "data": "0010FABDDA0AB00D1D012388D7V00AD97F077A6D097123207DD1...",
                "uploaded_at": "2015-08-05T08:40:51.620Z",
                "contains_food": "Yes",
                "certainty": .75
            }
        ]

## AI Interface [/analyze]
### Analyze Image(s) [POST]

Upload and analyze a list of images with the seefood-ai. 
Return whether or not each image contains food and the certainty.
NOTE: The binary data of the images will not be returned for efficiency.

+ Request (application/json)

        [
            {
                "name": "banana",
                "type": "png",
                "data": "AB00234AFDFDAD2002340F0011000000100100011AE324FFAD32..."
            },
            {
                "name": "car",
                "type": "png",
                "data": "AB00234AFDFDAD2002340F0011000000100100011AE324FFAD32..."
            }
        ]

+ Response 201 (application/json)
    + Body

            [
                {   
                    "name": "banana",
                    "type": "png",
                    "contains_food": "Yes",
                    "certainty": .95
                },
                {
                    "name": "car",
                    "type": "png",
                    "contains_food": "No",
                    "certainty": .66
                }
]









