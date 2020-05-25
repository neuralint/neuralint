<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
    <graph role="graph" edgeids="false" edgemode="directed" id="dataNew">
        <attr name="$version">
            <string>curly</string>
        </attr>
        <node id="n0">
            <attr name="layout">
                <string>55 13 88 18</string>
            </attr>
        </node>
        <node id="n1">
            <attr name="layout">
                <string>10 150 29 18</string>
            </attr>
        </node>
        <node id="n2">
            <attr name="layout">
                <string>75 183 46 18</string>
            </attr>
        </node>
        <node id="n3">
            <attr name="layout">
                <string>153 226 129 36</string>
            </attr>
        </node>
        <node id="n4">
            <attr name="layout">
                <string>311 27 66 72</string>
            </attr>
        </node>
        <node id="n5">
            <attr name="layout">
                <string>610 25 93 90</string>
            </attr>
        </node>
        <node id="n6">
            <attr name="layout">
                <string>389 140 40 36</string>
            </attr>
        </node>
        <node id="n7">
            <attr name="layout">
                <string>465 203 39 36</string>
            </attr>
        </node>
        <node id="n8">
            <attr name="layout">
                <string>549 234 66 36</string>
            </attr>
        </node>
        <node id="n9">
            <attr name="layout">
                <string>739 220 51 36</string>
            </attr>
        </node>
        <node id="n10">
            <attr name="layout">
                <string>646 204 56 36</string>
            </attr>
        </node>
        <node id="n11">
            <attr name="layout">
                <string>1141 28 93 90</string>
            </attr>
        </node>
        <node id="n12">
            <attr name="layout">
                <string>848 159 84 36</string>
            </attr>
        </node>
        <node id="n13">
            <attr name="layout">
                <string>792 106 56 36</string>
            </attr>
        </node>
        <node id="n14">
            <attr name="layout">
                <string>1049 162 41 36</string>
            </attr>
        </node>
        <node id="n15">
            <attr name="layout">
                <string>1071 323 93 90</string>
            </attr>
        </node>
        <node id="n16">
            <attr name="layout">
                <string>904 266 40 36</string>
            </attr>
        </node>
        <node id="n17">
            <attr name="layout">
                <string>1229 202 39 36</string>
            </attr>
        </node>
        <node id="n18">
            <attr name="layout">
                <string>985 226 66 36</string>
            </attr>
        </node>
        <node id="n19">
            <attr name="layout">
                <string>935 439 51 36</string>
            </attr>
        </node>
        <node id="n20">
            <attr name="layout">
                <string>900 356 56 36</string>
            </attr>
        </node>
        <node id="n21">
            <attr name="layout">
                <string>1034 630 93 90</string>
            </attr>
        </node>
        <node id="n22">
            <attr name="layout">
                <string>1122 508 84 36</string>
            </attr>
        </node>
        <node id="n23">
            <attr name="layout">
                <string>1203 584 56 36</string>
            </attr>
        </node>
        <node id="n24">
            <attr name="layout">
                <string>968 534 41 36</string>
            </attr>
        </node>
        <node id="n25">
            <attr name="layout">
                <string>814 654 42 54</string>
            </attr>
        </node>
        <node id="n26">
            <attr name="layout">
                <string>813 549 35 36</string>
            </attr>
        </node>
        <node id="n27">
            <attr name="layout">
                <string>490 646 93 90</string>
            </attr>
        </node>
        <node id="n28">
            <attr name="layout">
                <string>579 485 31 36</string>
            </attr>
        </node>
        <node id="n29">
            <attr name="layout">
                <string>484 479 46 36</string>
            </attr>
        </node>
        <node id="n30">
            <attr name="layout">
                <string>660 493 56 36</string>
            </attr>
        </node>
        <node id="n31">
            <attr name="layout">
                <string>326 509 115 36</string>
            </attr>
        </node>
        <node id="n32">
            <attr name="layout">
                <string>148 611 93 90</string>
            </attr>
        </node>
        <node id="n33">
            <attr name="layout">
                <string>36 582 31 36</string>
            </attr>
        </node>
        <node id="n34">
            <attr name="layout">
                <string>123 504 39 36</string>
            </attr>
        </node>
        <edge from="n0" to="n0">
            <attr name="label">
                <string>type:DNN-program</string>
            </attr>
        </edge>
        <edge from="n0" to="n3">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n1">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n2">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n1" to="n1">
            <attr name="label">
                <string>type:Data</string>
            </attr>
        </edge>
        <edge from="n2" to="n2">
            <attr name="label">
                <string>type:Learner</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>type:Model</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>let:hiddenLayerCount = int:6</string>
            </attr>
        </edge>
        <edge from="n3" to="n4">
            <attr name="label">
                <string>starts</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>type:InputLayer</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:No = int:1</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:size = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n4" to="n5">
            <attr name="label">
                <string>has-some</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:No = int:2</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:inputSize = string:"n1"</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:size = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n5" to="n8">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n5" to="n6">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n5" to="n9">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n5" to="n7">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n5" to="n10">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n5" to="n11">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n6" to="n6">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n6" to="n6">
            <attr name="label">
                <string>flag:conv2d</string>
            </attr>
        </edge>
        <edge from="n7" to="n7">
            <attr name="label">
                <string>type:filters</string>
            </attr>
        </edge>
        <edge from="n7" to="n7">
            <attr name="label">
                <string>flag:32</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>type:kernel_size</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>flag:(5, 5)</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>type:padding</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>flag:same</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:No = int:3</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:inputSize = string:"n2"</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:size = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n11" to="n15">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n11" to="n13">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n11" to="n14">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n11" to="n12">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>flag:max_pooling2d</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>type:pool_size</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>flag:(2, 2)</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>type:strides</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>flag:2</string>
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
                <string>let:No = int:4</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:inputSize = string:"n3"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:size = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n15" to="n20">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n15" to="n19">
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
        <edge from="n15" to="n21">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n15" to="n18">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>flag:conv2d</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>type:filters</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>flag:64</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>type:kernel_size</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>flag:(5, 5)</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>type:padding</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>flag:same</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>let:No = int:5</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>let:inputSize = string:"n4"</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>let:size = string:"n5"</string>
            </attr>
        </edge>
        <edge from="n21" to="n22">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n21" to="n23">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n21" to="n24">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n21" to="n25">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>flag:max_pooling2d</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>type:pool_size</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>flag:(2, 2)</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>type:strides</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>flag:2</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>let:No = int:6</string>
            </attr>
        </edge>
        <edge from="n25" to="n27">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n25" to="n26">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>flag:flatten</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>flag:done</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:No = int:7</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:inputSize = string:"n6"</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:size = string:"n7"</string>
            </attr>
        </edge>
        <edge from="n27" to="n32">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n27" to="n31">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n28">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n29">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n30">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>type:units</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>flag:512</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>type:Activator</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>flag:relu</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>type:Regularizer</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>let:dropoutRate = real:0.25</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>flag:output</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>let:No = int:8</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>let:inputSize = string:"n7"</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>let:size = string:"n8"</string>
            </attr>
        </edge>
        <edge from="n32" to="n33">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n32" to="n34">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>type:Type</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>flag:dense</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>type:units</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>flag:10</string>
            </attr>
        </edge>
    </graph>
</gxl>
