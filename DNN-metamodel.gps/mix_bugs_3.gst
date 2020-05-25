<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<gxl xmlns="http://www.gupro.de/GXL/gxl-1.0.dtd">
    <graph role="graph" edgeids="false" edgemode="directed" id="mix_bugs_3">
        <attr name="$version">
            <string>curly</string>
        </attr>
        <node id="n0"/>
        <node id="n1"/>
        <node id="n2"/>
        <node id="n3"/>
        <node id="n4"/>
        <node id="n5"/>
        <node id="n6"/>
        <node id="n7"/>
        <node id="n8"/>
        <node id="n9"/>
        <node id="n10"/>
        <node id="n11"/>
        <node id="n12"/>
        <node id="n13"/>
        <node id="n14"/>
        <node id="n15"/>
        <node id="n16"/>
        <node id="n17"/>
        <node id="n18"/>
        <node id="n19"/>
        <node id="n20"/>
        <node id="n21"/>
        <node id="n22"/>
        <node id="n23"/>
        <node id="n24"/>
        <node id="n25"/>
        <node id="n26"/>
        <node id="n27"/>
        <node id="n28"/>
        <node id="n29"/>
        <node id="n30"/>
        <node id="n31"/>
        <node id="n32"/>
        <node id="n33"/>
        <node id="n34"/>
        <node id="n35"/>
        <node id="n36"/>
        <node id="n37"/>
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
        <edge from="n0" to="n33">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n0" to="n0">
            <attr name="label">
                <string>type:DNN-program</string>
            </attr>
        </edge>
        <edge from="n1" to="n1">
            <attr name="label">
                <string>type:Data</string>
            </attr>
        </edge>
        <edge from="n2" to="n2">
            <attr name="label">
                <string>type:Architecture</string>
            </attr>
        </edge>
        <edge from="n2" to="n3">
            <attr name="label">
                <string>starts</string>
            </attr>
        </edge>
        <edge from="n2" to="n2">
            <attr name="label">
                <string>let:hiddenLayerCount = int:10</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>let:dim2 = int:28</string>
            </attr>
        </edge>
        <edge from="n3" to="n4">
            <attr name="label">
                <string>followed-by</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>let:channels = int:1</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>type:InputLayer</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>let:dim1 = int:28</string>
            </attr>
        </edge>
        <edge from="n3" to="n3">
            <attr name="label">
                <string>let:No = int:0</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:in_dim3 = int:1</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:in_dim2 = int:28</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:out_dim2 = int:28</string>
            </attr>
        </edge>
        <edge from="n4" to="n8">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n4" to="n7">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n4" to="n6">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n4" to="n5">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:in_dim1 = int:28</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:out_dim3 = int:32</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:No = int:1</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:out_dim1 = int:28</string>
            </attr>
        </edge>
        <edge from="n4" to="n4">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:padding = string:"same"</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:strides_dim1 = int:1</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:strides_dim2 = int:1</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:kernel_dim1 = int:5</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:type = string:"conv2d"</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:filters = int:32</string>
            </attr>
        </edge>
        <edge from="n5" to="n5">
            <attr name="label">
                <string>let:kernel_dim2 = int:5</string>
            </attr>
        </edge>
        <edge from="n6" to="n6">
            <attr name="label">
                <string>type:Weights</string>
            </attr>
        </edge>
        <edge from="n6" to="n6">
            <attr name="label">
                <string>let:initializer = string:"glorot_uniform"</string>
            </attr>
        </edge>
        <edge from="n7" to="n7">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n7" to="n7">
            <attr name="label">
                <string>let:initializer = string:"zeros"</string>
            </attr>
        </edge>
        <edge from="n8" to="n10">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:in_dim3 = int:32</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:out_dim1 = int:14</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:No = int:2</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:in_dim1 = int:28</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:out_dim3 = int:32</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:in_dim2 = int:28</string>
            </attr>
        </edge>
        <edge from="n8" to="n9">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:out_dim2 = int:14</string>
            </attr>
        </edge>
        <edge from="n8" to="n8">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:pool_dim2 = int:2</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:strides_dim1 = int:2</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:strides_dim2 = int:2</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:padding = string:"valid"</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:pool_dim1 = int:2</string>
            </attr>
        </edge>
        <edge from="n9" to="n9">
            <attr name="label">
                <string>let:type = string:"max_pooling2d"</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:No = int:3</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:out_dim1 = int:14</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:in_dim3 = int:32</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:out_dim3 = int:64</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n10" to="n11">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:in_dim1 = int:14</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:in_dim2 = int:14</string>
            </attr>
        </edge>
        <edge from="n10" to="n14">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n10" to="n13">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n10" to="n10">
            <attr name="label">
                <string>let:out_dim2 = int:14</string>
            </attr>
        </edge>
        <edge from="n10" to="n12">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:strides_dim1 = int:1</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:kernel_dim2 = int:5</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:kernel_dim1 = int:5</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:strides_dim2 = int:1</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:type = string:"conv2d"</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:padding = string:"same"</string>
            </attr>
        </edge>
        <edge from="n11" to="n11">
            <attr name="label">
                <string>let:filters = int:64</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>let:initializer = string:"glorot_uniform"</string>
            </attr>
        </edge>
        <edge from="n12" to="n12">
            <attr name="label">
                <string>type:Weights</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n13" to="n13">
            <attr name="label">
                <string>let:initializer = string:"zeros"</string>
            </attr>
        </edge>
        <edge from="n14" to="n16">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n14" to="n15">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:in_dim2 = int:14</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:No = int:4</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:in_dim1 = int:14</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:out_dim3 = int:64</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:out_dim2 = int:7</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:out_dim1 = int:7</string>
            </attr>
        </edge>
        <edge from="n14" to="n14">
            <attr name="label">
                <string>let:in_dim3 = int:64</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:pool_dim1 = int:2</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:padding = string:"valid"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:strides_dim2 = int:2</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:type = string:"max_pooling2d"</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:pool_dim2 = int:2</string>
            </attr>
        </edge>
        <edge from="n15" to="n15">
            <attr name="label">
                <string>let:strides_dim1 = int:2</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n16" to="n17">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:No = int:5</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:out_dim1 = int:3136</string>
            </attr>
        </edge>
        <edge from="n16" to="n18">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:in_dim1 = int:7</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:in_dim3 = int:64</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:in_dim2 = int:7</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n16" to="n16">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>let:type = string:"flatten"</string>
            </attr>
        </edge>
        <edge from="n17" to="n17">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n18" to="n21">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>let:No = int:6</string>
            </attr>
        </edge>
        <edge from="n18" to="n19">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>let:out_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n18" to="n20">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n18" to="n22">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n18" to="n18">
            <attr name="label">
                <string>let:in_dim1 = int:3136</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n19" to="n19">
            <attr name="label">
                <string>let:type = string:"dense"</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>let:initializer = string:"constant"</string>
            </attr>
        </edge>
        <edge from="n20" to="n20">
            <attr name="label">
                <string>type:Weights</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n21" to="n21">
            <attr name="label">
                <string>let:initializer = string:"zeros"</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n22" to="n23">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>let:in_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>let:out_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n22" to="n24">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>let:No = int:7</string>
            </attr>
        </edge>
        <edge from="n22" to="n22">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>let:activation = string:"relu"</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>let:nonLinear = true</string>
            </attr>
        </edge>
        <edge from="n23" to="n23">
            <attr name="label">
                <string>let:type = string:"activator"</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:in_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:out_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n24" to="n25">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n24" to="n26">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n24" to="n24">
            <attr name="label">
                <string>let:No = int:8</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>let:dropoutRate = real:0.25</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n25" to="n25">
            <attr name="label">
                <string>let:type = string:"dropout"</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n26" to="n27">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n26" to="n30">
            <attr name="label">
                <string>next</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:out_dim1 = int:10</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:No = int:9</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n26" to="n26">
            <attr name="label">
                <string>let:in_dim1 = int:512</string>
            </attr>
        </edge>
        <edge from="n26" to="n29">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n26" to="n28">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n27" to="n27">
            <attr name="label">
                <string>let:type = string:"dense"</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>type:Weights</string>
            </attr>
        </edge>
        <edge from="n28" to="n28">
            <attr name="label">
                <string>let:initializer = string:"constant"</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>type:Bias</string>
            </attr>
        </edge>
        <edge from="n29" to="n29">
            <attr name="label">
                <string>let:initializer = string:"zeros"</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>type:Layer</string>
            </attr>
        </edge>
        <edge from="n30" to="n32">
            <attr name="label">
                <string>ends</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>flag:output</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>let:No = int:10</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>let:in_dim1 = int:10</string>
            </attr>
        </edge>
        <edge from="n30" to="n31">
            <attr name="label">
                <string>has-a</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>let:out_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>let:in_dim0 = int:32</string>
            </attr>
        </edge>
        <edge from="n30" to="n30">
            <attr name="label">
                <string>let:out_dim1 = int:10</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>let:nonLinear = true</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>let:activation = string:"softmax"</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>type:Parameters</string>
            </attr>
        </edge>
        <edge from="n31" to="n31">
            <attr name="label">
                <string>let:type = string:"activator"</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>type:Labels</string>
            </attr>
        </edge>
        <edge from="n32" to="n32">
            <attr name="label">
                <string>let:size = int:10</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:loop_line_start = int:66</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:loop_line_end = int:91</string>
            </attr>
        </edge>
        <edge from="n33" to="n37">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>type:Learner</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:global_initializer = true</string>
            </attr>
        </edge>
        <edge from="n33" to="n34">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n33" to="n33">
            <attr name="label">
                <string>let:location_of_initializer = int:65</string>
            </attr>
        </edge>
        <edge from="n33" to="n36">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n33" to="n35">
            <attr name="label">
                <string>has</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:input_type = string:"pre_activation"</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:predictions = int:10</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:type = string:"softmax_cross_entropy"</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>type:Loss</string>
            </attr>
        </edge>
        <edge from="n34" to="n34">
            <attr name="label">
                <string>let:problem_type = string:"classification"</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>let:type = string:"adam"</string>
            </attr>
        </edge>
        <edge from="n35" to="n35">
            <attr name="label">
                <string>type:Optimizer</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>let:batchSize = int:32</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>type:Hyperparameters</string>
            </attr>
        </edge>
        <edge from="n36" to="n36">
            <attr name="label">
                <string>let:epochCount = int:100</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>type:Metric</string>
            </attr>
        </edge>
        <edge from="n37" to="n37">
            <attr name="label">
                <string>let:type = string:"accuracy"</string>
            </attr>
        </edge>
    </graph>
</gxl>
