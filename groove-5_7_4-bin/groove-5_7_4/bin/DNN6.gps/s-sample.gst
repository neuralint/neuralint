<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
    <graph role="graph" edgeids="false" edgemode="directed" id="s-sample">
        <attr name="$version">
            <string>curly</string>
        </attr>
        <node id="n0">
            <attr name="layout">
                <string>29 29 88 18</string>
            </attr>
        </node>
        <node id="n11">
            <attr name="layout">
                <string>215 137 129 36</string>
            </attr>
        </node>
        <node id="n12">
            <attr name="layout">
                <string>36 187 46 18</string>
            </attr>
        </node>
        <node id="n13">
            <attr name="layout">
                <string>382 11 66 72</string>
            </attr>
        </node>
        <node id="n15">
            <attr name="layout">
                <string>913 62 93 90</string>
            </attr>
        </node>
        <node id="n16">
            <attr name="layout">
                <string>1150 163 56 36</string>
            </attr>
        </node>
        <node id="n17">
            <attr name="layout">
                <string>1113 26 25 18</string>
            </attr>
        </node>
        <node id="n18">
            <attr name="layout">
                <string>1058 212 64 36</string>
            </attr>
        </node>
        <node id="n19">
            <attr name="layout">
                <string>967 224 58 36</string>
            </attr>
        </node>
        <node id="n20">
            <attr name="layout">
                <string>1138 80 108 36</string>
            </attr>
        </node>
        <node id="n21">
            <attr name="layout">
                <string>799 37 31 36</string>
            </attr>
        </node>
        <node id="n24">
            <attr name="layout">
                <string>699 418 93 90</string>
            </attr>
        </node>
        <node id="n25">
            <attr name="layout">
                <string>1215 314 56 36</string>
            </attr>
        </node>
        <node id="n26">
            <attr name="layout">
                <string>951 562 25 18</string>
            </attr>
        </node>
        <node id="n27">
            <attr name="layout">
                <string>1089 305 64 36</string>
            </attr>
        </node>
        <node id="n28">
            <attr name="layout">
                <string>681 260 58 36</string>
            </attr>
        </node>
        <node id="n29">
            <attr name="layout">
                <string>393 217 108 36</string>
            </attr>
        </node>
        <node id="n30">
            <attr name="layout">
                <string>1251 458 31 36</string>
            </attr>
        </node>
        <node id="n34">
            <attr name="layout">
                <string>328 457 93 90</string>
            </attr>
        </node>
        <node id="n35">
            <attr name="layout">
                <string>179 487 56 36</string>
            </attr>
        </node>
        <node id="n36">
            <attr name="layout">
                <string>200 434 25 18</string>
            </attr>
        </node>
        <node id="n37">
            <attr name="layout">
                <string>187 370 64 36</string>
            </attr>
        </node>
        <node id="n38">
            <attr name="layout">
                <string>319 369 58 36</string>
            </attr>
        </node>
        <node id="n39">
            <attr name="layout">
                <string>386 645 108 36</string>
            </attr>
        </node>
        <node id="n40">
            <attr name="layout">
                <string>272 609 31 36</string>
            </attr>
        </node>
        <node id="n44">
            <attr name="layout">
                <string>839 616 93 108</string>
            </attr>
        </node>
        <node id="n45">
            <attr name="layout">
                <string>1055 813 56 36</string>
            </attr>
        </node>
        <node id="n46">
            <attr name="layout">
                <string>1011 830 25 18</string>
            </attr>
        </node>
        <node id="n47">
            <attr name="layout">
                <string>1054 725 64 36</string>
            </attr>
        </node>
        <node id="n48">
            <attr name="layout">
                <string>733 781 58 36</string>
            </attr>
        </node>
        <node id="n49">
            <attr name="layout">
                <string>1085 631 108 36</string>
            </attr>
        </node>
        <node id="n50">
            <attr name="layout">
                <string>880 812 31 36</string>
            </attr>
        </node>
        <edge from="n0" to="n0">
            <attr name="label">
                <string>type:DNN-program</string>
            </attr>
        </edge>
        <edge from="n0" to="n11">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n12">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>type:Model</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:hiddenLayerCount = int:3</string>
            </attr>
        </edge>
        <edge from="n11" to="n13">
            <attr name="label">
                <string>starts</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>type:Learner</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>type:InputLayer</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>let:No = int:1</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>let:size = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n13" to="n15">
            <attr name="label">
                <string>has-some</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:No = int:2</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:inputSize = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:size = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n15" to="n21">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n24">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n15" to="n18">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n20">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n16">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n17">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n19">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>type:Constraint</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>flag:MaxNorm</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>flag:constant</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:No = int:3</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:inputSize = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:size = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n24" to="n34">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n24" to="n30">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n28">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n25">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n26">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n29">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n27">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>type:Constraint</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:MaxNorm</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>flag:constant</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:No = int:4</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:inputSize = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:size = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n34" to="n35">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n37">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n39">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n40">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n44">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n34" to="n38">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n34" to="n36">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>type:Constraint</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>flag:MaxNorm</string>
            </attr>
        </edge>
        <edge from="n38" to="n38">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n38" to="n38">
            <attr name="label">
                <string>flag:constant</string>
            </attr>
        </edge>
        <edge from="n39" to="n39">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n39" to="n39">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
        <edge from="n40" to="n40">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n40" to="n40">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>flag:end</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>flag:output</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>let:No = int:5</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>let:inputSize = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n44" to="n44">
            <attr name="label">
                <string>let:size = string:"n5"</string>
            </attr>
        </edge>
        <edge from="n44" to="n47">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n44" to="n49">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n44" to="n45">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n44" to="n50">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n44" to="n48">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n44" to="n46">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n45" to="n45">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n45" to="n45">
            <attr name="label">
                <string>flag:softmax</string>
            </attr>
        </edge>
        <edge from="n46" to="n46">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n47" to="n47">
            <attr name="label">
                <string>type:Constraint</string>
            </attr>
        </edge>
        <edge from="n47" to="n47">
            <attr name="label">
                <string>flag:MaxNorm</string>
            </attr>
        </edge>
        <edge from="n48" to="n48">
            <attr name="label">
                <string>type:Initializer</string>
            </attr>
        </edge>
        <edge from="n48" to="n48">
            <attr name="label">
                <string>flag:constant</string>
            </attr>
        </edge>
        <edge from="n49" to="n49">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n49" to="n49">
            <attr name="label">
                <string>let:dropoutRate = real:0.4</string>
            </attr>
        </edge>
        <edge from="n50" to="n50">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n50" to="n50">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
    </graph>
</gxl>
