from Products.CMFPlone import MigrationTool #:wort registerSetupWidget
from languages import LocalizerLanguageSetup
from skins import SkinsSetup
from customization_policy import CustomizationPolicySetup

MigrationTool.registerSetupWidget(LocalizerLanguageSetup)
MigrationTool.registerSetupWidget(SkinsSetup)
MigrationTool.registerSetupWidget(CustomizationPolicySetup)

