'''
This module is the main module that collects all core functionality that can be used in GUI mode.
'''
import datetime

import maya.cmds as cmds

import components as com
import fileSystem as fs
import mathExtended as mx
import ui.playblast as pb
import modeling as mdl
import pivot as piv


def createRunTimeCommand(commandName, annotation, command, category):
    if not cmds.runTimeCommand(commandName, exists=True):
        cmds.runTimeCommand(commandName,
                            annotation=annotation,
                            command=command,
                            category=category,
                            default=True)


def initializeRuntimeCommands():
    '''
    creates all runtimeCommands
    '''
    category = "FC-Tools.File"
    createRunTimeCommand(commandName="fcSmartOpen",
                         annotation="open a maya file and try to guess the project along the way",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.smartOpen()"),
                         category=category)

    createRunTimeCommand(commandName="fcReloadScene",
                         annotation="Reload the currently open scene.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.reloadScene()"),
                         category=category)

    createRunTimeCommand(commandName="fcSaveIncremental",
                         annotation="save the current maya file under a new version",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.saveIncremental()"),
                         category=category)

    createRunTimeCommand(commandName="fcSaveSnapshot",
                         annotation="create a snapshot of the vieport and save it in the render folder.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.saveSnapshot()"),
                         category=category)

    createRunTimeCommand(commandName="fcOpenSceneFolder",
                         annotation="open the current folder from this maya scene",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.openSceneFolder()"),
                         category=category)

    createRunTimeCommand(commandName="fcOpenRenderFolder",
                         annotation="open the folder where images will be rendered to",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.openRenderFolder()"),
                         category=category)

    createRunTimeCommand(commandName="fcOpenTextureFolder",
                         annotation="open the texture folder",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.openTextureFolder()"),
                         category=category)

    category = "FC-Tools.Selection"
    createRunTimeCommand(commandName="fcSelectTriangles",
                         annotation="select all triangles based on your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectTriangles()"),
                         category=category)

    createRunTimeCommand(commandName="fcSelectNGons",
                         annotation="select all n-gons based on your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectNGons()"),
                         category=category)

    createRunTimeCommand(commandName="fcSelectLaminaFaces",
                         annotation="select all lamina faces in your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectLaminaFaces()"),
                         category=category)

    createRunTimeCommand(commandName="fcSelectNonManifoldVertices",
                         annotation="select all non-manifold vertices in your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectNonManifoldVertices()"),
                         category=category)

    createRunTimeCommand(commandName="fcSelectUVSeams",
                         annotation="select all uv-seams in your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectUVSeams()"),
                         category=category)

    createRunTimeCommand(commandName="fcSelectHardEdges",
                         annotation="select all hard edges in your current selection",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.selectHardEdges()"),
                         category=category)

    category = "FC-Tools.Modeling"
    createRunTimeCommand(commandName="fcSpherify",
                         annotation="Move all selected components to equal distance to each other.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.spherify()"),
                         category=category)

    createRunTimeCommand(commandName="fcMoveComponentsToXAxis",
                         annotation="Move all selected components so they're aligned on the x-axis.",
                         command=('import maya.cmds as cmds\n'
                                  'cmds.fcAverageComponents(axis="x")'),
                         category=category)

    createRunTimeCommand(commandName="fcMoveComponentsToYAxis",
                         annotation="Move all selected components so they're aligned on the y-axis.",
                         command=('import maya.cmds as cmds\n'
                                  'cmds.fcAverageComponents(axis="y")'),
                         category=category)

    createRunTimeCommand(commandName="fcMoveComponentsToZAxis",
                         annotation="Move all selected components so they're aligned on the z-axis.",
                         command=('import maya.cmds as cmds\n'
                                  'cmds.fcAverageComponents(axis="z")'),
                         category=category)

    createRunTimeCommand(commandName="fcAssignDefaultShaderToSelection",
                         annotation='Assign the Default Shader "lambert1" to all selected objects.',
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.assignDefaultShaderToSelection()"),
                         category=category)

    createRunTimeCommand(commandName="fcToggleXrayDisplayOfSelection",
                         annotation="Toggle X-Ray display in the viewport on all selected objects.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.toggleXrayDisplayOfSelection()"),
                         category=category)

    category = "FC-Tools.Pivots"
    createRunTimeCommand(commandName="fcCopyPivot",
                         annotation="Copies the pivot of the selected object.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.copyPivot()"),
                         category=category)

    createRunTimeCommand(commandName="fcPastePivot",
                         annotation="Pastes the pivot to all selected objects.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.pastePivot()"),
                         category=category)

    createRunTimeCommand(commandName="fcPivotsToWorldCenter",
                         annotation="Moves the pivots of all selected objects to the world-center.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.pivotsToWorldCenter()"),
                         category=category)

    createRunTimeCommand(commandName="fcPivotToSelection",
                         annotation="Moves the pivot to the middle of the selected components.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.pivotToComponentSelection()"),
                         category=category)

    category = "FC-Tools.Display"
    createRunTimeCommand(commandName="fcToggleSmoothShaded",
                         annotation="Toggles smooth shading in the current viewport.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.toggleSmoothShaded()"),
                         category=category)

    createRunTimeCommand(commandName="fcToggleWireframe",
                         annotation="Toggles wireframe in the current viewport.",
                         command=("import fcore.fcontroller as fctl\n"
                                  "fctl.toggleWireframe()"),
                         category=category)


def smartOpen():
    fileBefore = cmds.file(q=True, sn=True)
    cmds.OpenScene()
    fileAfter = cmds.file(q=True, sn=True)

    if fileBefore != fileAfter:
        try:
            workspaceDir = fs.findWorkspace(fileAfter)
            cmds.workspace(workspaceDir, o=True)
            print "The Project was set to: " + workspaceDir,
        except OSError:
            cmds.warning("No Project-Directory found.")


def reloadScene():
    mayaFile = cmds.file(q=True, sn=True)
    if mayaFile:
        if "Yes" == cmds.confirmDialog(title='Reload Scene',
                                       message=('Are you sure you want to '
                                                'reload the Scene?'),
                                       button=['Yes', 'No'],
                                       defaultButton='No',
                                       cancelButton='No',
                                       dismissString='No'):
            cmds.file(mayaFile, open=True, force=True)
    else:
        cmds.warning("Your scene has not been saved yet!")


def saveIncremental():
    fs.incremental_save()


def openSceneFolder():
    mayaFile = cmds.file(q=True, sn=True)
    if mayaFile:
        fs.openExplorer(mayaFile)
    else:
        cmds.warning("Your scene has not been saved yet!")


def openRenderFolder():
    renderFolder = fs.getRenderFolder()
    fs.openExplorer(renderFolder)
    print "Opened Folder: " + renderFolder


def openTextureFolder():
    texFolder = fs.getSourceimagesFolder()
    fs.openExplorer(texFolder)
    print "Opened Folder: " + texFolder


def selectTriangles():
    tris = com.getTriangles()
    if tris:
        objs = list(set([tri.split('.')[0] for tri in tris]))
        cmds.select(tris)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print "Selected {0:d} Triangles.\n".format(len(tris)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not contain Triangles!\n",


def selectNGons():
    ngons = com.getNGons()
    if ngons:
        objs = list(set([ngon.split('.')[0] for ngon in ngons]))
        cmds.select(ngons)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print "Selected {0:d} N-Gons.\n".format(len(ngons)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not contain N-Gons!\n",


def selectLaminaFaces():
    lamina = com.getLaminaFaces()
    if lamina:
        objs = list(set([l.split('.')[0] for l in lamina]))
        cmds.select(lamina)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshFace=True)
        print "Selected {0:d} lamina faces.\n".format(len(lamina)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not contain lamina faces!\n",


def selectNonManifoldVertices():
    nmv = com.getNonManifoldVertices()
    if nmv:
        objs = list(set([vert.split('.')[0] for vert in nmv]))
        cmds.select(nmv)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, vertex=True)
        print "Selected {0:d} non-manifold vertices".format(len(nmv)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not contain non-manifold-vertices.",


def selectUVSeams():
    """
    select the UV Seams on all selected objects.
    """
    cmds.selectMode(object=True)

    seamEdges = []
    for obj in cmds.ls(selection=True):
        seamEdges += com.getSeamEdges(obj)
    if seamEdges:
        objs = list(set([edge.split('.')[0] for edge in seamEdges]))

        cmds.select(seamEdges)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshEdge=True)
        print "Selected {0:d} seam edges.\n".format(len(seamEdges)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not seam edges.\n",


def selectHardEdges():
    """
    select the hard edges on all selected objects.
    """
    cmds.selectMode(object=True)

    hardEdges = []
    for obj in cmds.ls(selection=True):
        hardEdges += com.getHardEdges(obj)
    if hardEdges:
        objs = list(set([edge.split('.')[0] for edge in hardEdges]))

        cmds.select(hardEdges)
        cmds.hilite(objs)
        cmds.selectMode(component=True)
        cmds.selectType(allComponents=False, polymeshEdge=True)
        print "Selected {0:d} hard edges.\n".format(len(hardEdges)),
    else:
        cmds.selectMode(object=True)
        print "Selection does not hard edges.\n",


def saveSnapshot(mode="project"):
    """
    save a snapshot from the current model panel.

    :param mode: "dialog": Save Snapshot with Dialog
                 "project": Save to Project Directory
                 "desktop": Save to Desktop
    """
    p = pb.getModelPanel()
    cam_name = cmds.modelEditor(p, q=True, camera=True)
    curr_file_name = cmds.file(q=True, sn=True, shn=True)
    nice_file_name = "{0:%Y%m%d_%H%M%S}_{1:s}_{2:s}".format(datetime.datetime.now(),
                                                            curr_file_name.strip(".ma"),
                                                            cam_name)

    desktopFolder = fs.getDesktopFolder()
    imageFile = desktopFolder + nice_file_name + ".jpg"
    if mode == "project":
        imagesFolder = fs.getRenderFolder()
        imageFile = imagesFolder + nice_file_name + ".jpg"
    elif mode == "dialog":
        imageFile = cmds.fileDialog2(cap="Save Screengrab",
                                     fileFilter="JPEG (*.jpg);;TIFF (*.tif)",
                                     startingDirectory=imageFile,
                                     fileMode=0,
                                     okCaption="Save",
                                     dialogStyle=2)
        if imageFile is not None:
            imageFile = imageFile[0]
        else:
            return
    print imageFile
    pb.createViewportSnapshot(imageFile)


def spherify():
    '''
    puts selected Components to average Distance to their Midpoint
    '''
    vertices = com.convertToVertices(cmds.ls(selection=True))

    positions = [cmds.pointPosition(vertex) for vertex in vertices]
    midpoint = mx.midpoint(positions)

    distances = [mx.distance(midpoint, pos) for pos in positions]
    averageDistance = mx.average(distances)

    newPositions = mx.spherify(positions, averageDistance)

    for vert, pos in zip(vertices, newPositions):
        cmds.move(pos[0], pos[1], pos[2], vert, a=True)


def copyPivot():
    sel = cmds.ls(selection=True, o=True)
    piv.copyPivot(sel[0])

    print "Saved Pivot from: " + sel[0],


def pastePivot():
    sel = cmds.ls(selection=True, o=True)
    for obj in sel:
        piv.pastePivot(obj)
    cmds.selectMode(object=True)

    print "Applied Pivot to:    " + str(sel),


def pivotToComponentSelection():
    """
    puts the Pivot to the current component selection
    """
    sel = cmds.ls(selection=True, fl=True)
    piv.pivotToComponents(sel)
    cmds.selectMode(object=True)


def pivotsToWorldCenter():
    """
    Moves all pivots from the selected objects to the world center
    """
    sel = cmds.ls(selection=True)
    for obj in sel:
        piv.pivotToWorldCenter(obj)


def toggleSmoothShaded():
    mdlEditor = pb.getModelPanel()
    if mdlEditor:
        pb.toggleSmoothShaded(mdlEditor)


def toggleWireframe():
    mdlEditor = pb.getModelPanel()
    if mdlEditor:
        pb.toggleWireframe(mdlEditor)


def assignDefaultShaderToSelection():
    cmds.sets(edit=True, forceElement="initialShadingGroup")


def toggleXrayDisplayOfSelection():
    '''
    Toggles the XRay display in the viewport of the selected objects.
    '''
    # this flag combination gives you all surface shapes below the selected surface shape
    sel = cmds.ls(selection=True, allPaths=True, dagObjects=True, type='surfaceShape')
    mdl.toggleXRayDisplay(objects=sel)